package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		t := scanner.Text()
		ts := strings.Split(t, ",")
		sort.Strings(ts)
		fmt.Printf("%s\n", strings.Join(ts, ","))
	}
}
