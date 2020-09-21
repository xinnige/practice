package main

import (
	"bufio"
	"fmt"
	"os"
)

func longestCommonStr(str1, str2 string) string {
	len1 := len(str1)
	len2 := len(str2)
	dynamic := make([][]int, len1)
	for i := 0; i < len1; i++ {
		dynamic[i] = make([]int, len2)
		for j := 0; j < len2; j++ {
			if str1[i] == str2[j] {
				if i > 0 && j > 0 {
					dynamic[i][j] = dynamic[i-1][j-1] + 1
				} else {
					dynamic[i][j] = 1
				}
			} else {
				dynamic[i][j] = 0
			}
		}
	}
	maxlen := 0
	maxi := 0
	for i := 0; i < len1; i++ {
		for j := 0; j < len2; j++ {
			if dynamic[i][j] > maxlen {
				maxlen = dynamic[i][j]
				maxi = i
			}
		}
	}
	if maxlen == 0 {
		return ""
	}
	fmt.Printf("%d, %d\n", maxi, maxlen)

	return str1[maxi-maxlen+1 : maxi+1]
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	str1 := scanner.Text()
	scanner.Scan()
	str2 := scanner.Text()
	if len(str1) < len(str2) {
		fmt.Printf("%s\n", longestCommonStr(str1, str2))
	} else {
		fmt.Printf("%s\n", longestCommonStr(str2, str1))
	}
}
