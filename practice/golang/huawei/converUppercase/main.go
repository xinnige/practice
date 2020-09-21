package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func toUpper(s string) string {
	ret := []byte(s)
	for i := range ret {
		if ret[i] == 'a' || ret[i] == 'i' || ret[i] == 'e' || ret[i] == 'o' || ret[i] == 'u' {
			ret[i] = byte(unicode.ToUpper(rune(s[i])))
		}
	}
	return fmt.Sprintf("%s", ret)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		text := scanner.Text()
		fmt.Printf("%s\n", toUpper(text))
	}
}
