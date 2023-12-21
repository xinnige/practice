package pprof

import (
	"fmt"
	"runtime"
)

func pporf() {
	fmt.Printf("%d", runtime.NumGoroutine())
}
