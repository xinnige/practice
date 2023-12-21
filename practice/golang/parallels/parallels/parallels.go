package parallel

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"net/http"
	"runtime/debug"
	"time"

	"github.com/pkg/errors"

	"github.com/google/wire"
	grpctags "github.com/grpc-ecosystem/go-grpc-middleware/tags"
	"github.com/sirupsen/logrus"
)

type ProxyService interface {
	ProxyAny(req *http.Request, targets []string, body []byte, tags grpctags.Tags) (int, []byte, http.Header, error)
}

var Provider = wire.NewSet(wire.Struct(new(Service), "*"), wire.Bind(new(ProxyService), NewService))

var _ ProxyService = NewService()

type Service struct {
	*http.Client
}

func NewService() *Service {
	return &Service{
		Client: http.DefaultClient,
	}
}

func (s Service) ProxyAny(req *http.Request, targets []string, body []byte, tags grpctags.Tags) (statusCode int, respBody []byte, respHeader http.Header, reterr error) {
	t1 := time.Now()

	tags.Set("reqSize", len(body))

	if len(targets) == 0 {
		return 0, nil, nil, errors.New("ErrNoProxyTarget")
	}

	// concurrenty
	chanResp := make(chan *http.Response)
	chanErr := make(chan error)
	errs := []error{}

	cctx, cancel := context.WithTimeout(context.Background(), time.Duration(5)*time.Second)
	defer cancel()

	for _, target := range targets {
		cReq, err := CloneRequest(cctx, req, target, body)
		if err != nil {
			return 0, nil, nil, fmt.Errorf("clone request err: %v", err)
		}

		go func(r *http.Request, gtags grpctags.Tags) {

			defer func() {
				if err := recover(); err != nil {
					logrus.WithField("stack", string(debug.Stack())).Errorf("recover from panic")
				}
			}()
			resp, err := s.do(r, t1, gtags)
			if err != nil {
				select {
				case chanErr <- err:
				case <-r.Context().Done():
					logrus.Debugf("proxy %s error: %v", r.URL.String(), context.Canceled)
				}
			} else {
				select {
				case chanResp <- resp:
				case <-r.Context().Done():
					logrus.Debugf("proxy %s error: %v", r.URL.String(), context.Canceled)
				}
			}
		}(cReq, CloneTags(tags))
	}

	for i := 0; i < len(targets); i++ {
		select {
		case <-req.Context().Done():
			logrus.Debugf("client %s canceled: %v, index at: %d", req.URL.String(), context.Canceled, i)
			return 0, nil, nil, context.Canceled
		case <-cctx.Done():
			logrus.Debugf("proxy %s canceled: %v, index at: %d", req.URL.String(), context.Canceled, i)
		case resp := <-chanResp:
			if resp != nil {
				statusCode = resp.StatusCode
				return ReadResponse(resp, tags)
			}
		case err := <-chanErr:
			errs = append(errs, err)
			logrus.WithField("err", err).Debugf("proxy %s canceled: %v, index at: %d", req.URL.String(), context.Canceled, i)
		}
	}
	if len(errs) != 0 {
		reterr = errors.Wrapf(errors.New("proxy error"), "errors:", errs)
	}
	return 0, nil, nil, reterr
}

func (s Service) do(req *http.Request, t1 time.Time, tags grpctags.Tags) (resp *http.Response, err error) {

	resp, err = s.Client.Do(req)
	if err != nil {
		if errors.Is(err, context.Canceled) {
			logrus.WithField("error", err).Debugf("fail to do http request %s, err: %v", req.URL.String(), err)
		}
		return nil, err
	}
	// defer resp.Body.Close()
	if resp.Request == nil {
		resp.Request = req
	}
	return resp, err
}

func CloneRequest(ctx context.Context, req *http.Request, targetURL string, body []byte) (*http.Request, error) {
	cReq, err := http.NewRequestWithContext(ctx, req.Method, targetURL, io.NopCloser(bytes.NewBuffer(body)))
	if err != nil {
		return nil, err
	}

	if req.Header != nil {
		cReq.Header = req.Header.Clone()
	}
	if req.Trailer != nil {
		cReq.Trailer = req.Trailer.Clone()
	}

	return cReq, nil
}

func ReadResponse(resp *http.Response, tags grpctags.Tags) (statusCode int, respBody []byte, headers http.Header, err error) {
	if resp.Body != nil {
		respBody, err = io.ReadAll(resp.Body)
		if err != nil {
			return 0, []byte{}, resp.Header, err
		}
		defer resp.Body.Close()
	}
	if resp.Request != nil {
		tags.Set("uri", resp.Request.URL.String())
	}
	return resp.StatusCode, respBody, resp.Header, nil
}

func CloneTags(tags grpctags.Tags) grpctags.Tags {
	newTags := grpctags.NewTags()
	for k, v := range tags.Values() {
		newTags.Set(k, v)
	}
	return newTags
}
