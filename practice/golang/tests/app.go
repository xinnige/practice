package main

import (
    "fmt"
    "log"
    "net/http"
    "github.com/go-redis/redis/v8"
)

func main() {
    client := redis.NewClient(&redis.Options{
        Addr: "db:6379",
        Password: "",
        DB: 0,
    })

    pong, err := client.Ping().Result()
    if err != nil {
        panic(err)
    }
    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "Hello, %q", pong)
    })

    log.Fatal(http.ListenAndServe(":5000", nil))

}
