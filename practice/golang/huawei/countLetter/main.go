package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func countLetter(s string, c byte) int {
	cnt := 0
	for i := range s {
		if unicode.ToLower(rune(s[i])) == unicode.ToLower(rune(c)) {
			cnt++
		}
	}
	return cnt
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	s := scanner.Text()
	scanner.Scan()
	c := scanner.Text()
	fmt.Printf("%d\n", countLetter(s, c[0]))
}
