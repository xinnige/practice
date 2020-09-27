package main

import (
	"fmt"
	"strconv"
)

func reversePositive(x int) []byte {
	digits := fmt.Sprintf("%d", x)
	nlen := len(digits)
	rev := make([]byte, nlen)
	for i := range digits {
		rev[i] = digits[nlen-1-i]
	}
	return rev
}

func reverse(x int) int {
	if x == 0 {
		return x
	}
	var rev []byte
	var ret int
	if x < 0 {
		rev = reversePositive(-x)
		ret, _ = strconv.Atoi(string(rev))
		if ret > 2147483648 {
			return 0
		}
		return 0 - ret

	}
	rev = reversePositive(x)
	ret, _ = strconv.Atoi(string(rev))
	if ret > 2147483647 {
		return 0
	}
	return ret
}

func main() {
	tests := []struct {
		integer int
		expect  int
	}{
		{-123, -321},
		{123, 321},
		{1000, 1},
		{120, 21},
		{-1000, -1},
		{2147483648, 0},
		{-2147483648, 0},
		{8463847412, 0},
		{7463847412, 2147483647},
	}
	for _, tc := range tests {
		fmt.Printf("reverse %d -> %d (expects %d)\n", tc.integer, reverse(tc.integer), tc.expect)
	}
}
