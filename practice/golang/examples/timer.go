package main

import (
    "fmt"
    "time"
)

func main() {
    start := time.Now()
    timer1 := time.NewTimer(5 * time.Second)
    <-timer1.C
    fmt.Println("It's time!")
    end := time.Now();
    fmt.Printf("%f秒\n",(end.Sub(start)).Seconds())
}
