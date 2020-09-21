package main

import (
	"bufio"
	"fmt"
	"os"
)

func fill(input string) string {
	binput := []byte(input)
	for i := len(input); i < 8; i++ {
		binput = append(binput, '0')
	}
	return fmt.Sprintf("%s", binput)
}

func split(s string) []string {
	slen := len(s) / 8
	smode := len(s) % 8
	if smode != 0 {
		slen = slen + 1
	}
	ret := make([]string, slen)
	i := 0
	for ; i < slen-1; i++ {
		ret[i] = s[i*8 : i*8+8]
	}
	ret[slen-1] = s[i*8:]
	if smode != 0 {
		ret[slen-1] = fill(ret[slen-1])
	}
	return ret
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		s := scanner.Text()
		if len(s) == 0 {
			fmt.Println(s)
		} else if len(s) < 8 {
			fmt.Println(fill(s))
		} else if len(s) > 8 {
			ss := split(s)
			for _, ones := range ss {
				fmt.Println(ones)
			}
		} else {
			fmt.Println(s)
		}
	}
}
