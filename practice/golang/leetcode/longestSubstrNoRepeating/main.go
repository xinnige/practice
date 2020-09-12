package main

import (
	"fmt"
)

func lengthOfLongestSubstring(s string) int {
	bmap := make(map[byte]int)
	maxlen := 0
	counter := 0
	for i := 0; i < len(s); i++ {
		if prev, ok := bmap[s[i]]; ok {
			// repeat happens
			if counter > maxlen {
				maxlen = counter
			}
			bmap = make(map[byte]int)
			counter = 0
			i = prev
		} else {
			// no repeat happens
			counter += 1
			bmap[s[i]] = i
		}
	}
	if counter > maxlen {
		return counter
	}
	return maxlen
}

func main() {
	input := "abcabcbb"
	fmt.Printf("%s:\n%d\n", input, lengthOfLongestSubstring(input))
}
