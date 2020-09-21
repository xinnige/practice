package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		t := scanner.Text()
		ts := strings.Split(t, " ")
		if len(ts) != 2 {
			return
		}
		n1, _ := strconv.Atoi(ts[0])
		n2, _ := strconv.Atoi(ts[1])
		fmt.Printf("%d\n", n1+n2)
	}

}
