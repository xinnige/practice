# Note: define variable _Commit/_BuildAt in main package

PWD = $(shell pwd)
git_commit := $(shell git rev-parse --short HEAD)
buildat := $(shell date +%s)

LD_FLAGS=-ldflags "-X main._Commit=$(git_commit) -X main._BuildAt=$(buildat) -s -w"

.PHONY: build lint test
test:
    go test -v -coverprofile=cover.out.tmp -coverpkg=./...  ./...
lint:
	golangci-lint --timeout 5m run --out-format checkstyle ./...
build:
	git config --global url."https://".insteadOf "https://"
	go env -w GOPROXY="https://goproxy.cn,direct"
	GOOS=linux GOARCH=amd64 go build -mod=readonly ${LD_FLAGS} -o ${PWD}/dist/vpn_dumper .
clean:
	rm -rf ${PWD}/dist

