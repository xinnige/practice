package main

import (
	"fmt"
)

func distributeCandies(candies []int) int {
	cmap := make(map[int]int)
	for i := range candies {
		cmap[candies[i]] += 1
	}
	kinds := len(cmap)
	if kinds >= len(candies)/2 {
		return len(candies) / 2
	}
	return kinds
}

func main() {
	tests := []struct {
		candies []int
		expect  int
	}{
		{[]int{1, 1, 2, 2, 3, 3}, 3},
		{[]int{1, 1, 2, 3}, 2},
	}
	for _, tc := range tests {
		fmt.Printf("%v -> %d (expects %d)\n", tc.candies, distributeCandies(tc.candies), tc.expect)
	}
}
