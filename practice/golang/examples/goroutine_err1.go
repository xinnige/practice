package main

import (
    "fmt"
    "math/rand"
    "time"
    "sync"
)

func fakeError(attempts int) error {
	rn := rand.Intn(attempts)
    if rn % 2 == 0 {
        return fmt.Errorf("rand even number error %d", rn)
        // return nil
    }
    return fmt.Errorf("rand odd number error %d", rn)
    // return nil
}

func main() {
	rand.Seed(time.Now().UnixNano())
    attempts := 10
    wg := sync.WaitGroup{}
    errchan := make(chan error, attempts)

    for i := 0; i < attempts; i++ {
        wg.Add(1)
        go func(n int){
            if e := fakeError(n); e != nil {
                errchan <- e
            }
            wg.Done()
        }(attempts)
    }
    wg.Wait()
    
    close(errchan)
    for err := range errchan {
        fmt.Println(err)
    }

    
}
