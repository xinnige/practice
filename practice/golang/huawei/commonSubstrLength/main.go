package main

import (
	"bufio"
	"fmt"
	"os"
)

func longestCommonStrLength(str1, str2 string) int {
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
	for i := 0; i < len1; i++ {
		for j := 0; j < len2; j++ {
			if dynamic[i][j] > maxlen {
				maxlen = dynamic[i][j]
			}
			fmt.Printf("%d ", dynamic[i][j])
		}
		fmt.Println()
	}
	return maxlen
}

// func commonLength(str1, str2 string, i, j int) int {
// 	cnt := 0
// 	for i < len(str1) && j < len(str2) {
// 		if str1[i] == str2[j] {
// 			i++
// 			j++
// 			cnt++
// 		} else {
// 			break
// 		}
// 	}
// 	return cnt
// }

// func longestCommonStrLength(str1, str2 string) int {
// 	cnt := 0
// 	for i := 0; i < len(str1); i++ {
// 		for j := 0; j < len(str2); j++ {
// 			if str1[i] == str2[j] {
// 				clen := commonLength(str1, str2, i, j)
// 				if clen > cnt {
// 					cnt = clen
// 				}
// 			}
// 		}
// 	}
// 	return cnt
// }

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	str1 := scanner.Text()
	scanner.Scan()
	str2 := scanner.Text()
	if len(str1) < len(str2) {
		fmt.Printf("%d\n", longestCommonStrLength(str1, str2))
	} else {
		fmt.Printf("%d\n", longestCommonStrLength(str2, str1))
	}
}
