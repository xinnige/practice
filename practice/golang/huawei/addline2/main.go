package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func calculate(t string) int {
	cnt := 0
	ts := strings.Split(t, " ")
	for _, s := range ts {
		n, _ := strconv.Atoi(s)
		cnt += n
	}
	return cnt
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		t := scanner.Text()
		fmt.Printf("%d\n", calculate(t))
	}

}
