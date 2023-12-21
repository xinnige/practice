package webserver

import (
	"context"
	"net/http"
	"os"
	"os/signal"
	"syscall"

	"github.com/gin-gonic/gin"
)

func start() {
	router := gin.Default()
	router.SetTrustedProxies([]string{"10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16"})
	router.RemoteIPHeaders = []string{"X-Forwarded-For", "X-From-Ip", "X-Real-Ip"}
	router.RedirectTrailingSlash = false
	router.NoRoute(norouteMiddleware, HandleNoRoute)

	httpServer := &http.Server{
		Addr:    "127.0.0.1:8088",
		Handler: router,
	}
	go func() {
		httpServer.ListenAndServe()
	}()

	sigChan := make(chan os.Signal, 1)
	signal.Reset(os.Interrupt, syscall.SIGTERM)
	signal.Notify(sigChan, syscall.SIGHUP, syscall.SIGINT, syscall.SIGTERM)

	<-sigChan

	httpServer.Shutdown(context.Background())
}

func norouteMiddleware(c *gin.Context) {
	c.Next()
}

func HandleNoRoute(c *gin.Context) {
	c.AbortWithStatusJSON(http.StatusNotFound, gin.H{"code": http.StatusNotFound, "errmsg": "404 not found"})

}
