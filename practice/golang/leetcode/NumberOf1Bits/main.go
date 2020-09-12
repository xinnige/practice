package main

import (
	"fmt"
)

// func hammingWeight(num uint32) int {
// 	count := 0
// 	for num > 0 {
// 		if num&1 == 1 {
// 			count++
// 		}
// 		num = num >> 1
// 	}
// 	return count
// }

func hammingWeight(num uint32) int {
	count := 0
	for num > 0 {
		num &= num - 1
		count++
	}
	return count
}

func main() {
	tests := []struct {
		input  uint32
		expect int
	}{
		{19, 3},
	}
	for _, tc := range tests {
		fmt.Printf("%d, %d, %d\n", tc.input, tc.expect, hammingWeight(tc.input))
	}
}
