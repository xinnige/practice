package main

import (
	"bufio"
	"fmt"
	"os"
)

func lastWordLength(words string) int {
	cnt := 0
	for i := len(words) - 1; i >= 0; i-- {
		if words[i] == '\n' {
			continue
		}
		if words[i] != ' ' {
			cnt++
		} else {
			break
		}
		//fmt.Printf("index %d, cnt %d\n", i, cnt)
	}
	return cnt
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	fmt.Printf("%s length: %d", input, len(input))
	fmt.Printf("%d\n", lastWordLength(string(input)))
}
