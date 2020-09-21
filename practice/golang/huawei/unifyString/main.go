package main

import (
	"bufio"
	"fmt"
	"os"
)

func codeString(s string) string {
	ret := ""
	p := ""
	var cnt int
	for i := range s {
		if p != string([]byte{s[i]}) {
			if cnt != 0 {
				ret += fmt.Sprintf("%d%s", cnt, p)
			}
			cnt = 1
			p = string([]byte{s[i]})
		} else {
			cnt++
		}
	}
	return ret + fmt.Sprintf("%d%s", cnt, p)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	text := scanner.Text()
	fmt.Println(codeString(text))
}
