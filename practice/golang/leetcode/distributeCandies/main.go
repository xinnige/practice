package main

import (
	"fmt"
)

func distributeCandies(candies int, num_people int) []int {
	distcandy := make([]int, num_people)
	c := 1
	i := 0
	for candies > 0 {
		if candies < c {
			c = candies
		}
		if i == num_people {
			i = 0
		}
		distcandy[i] += c
		candies -= c
		i++
		c++
	}
	return distcandy
}

func main() {
	tests := []struct {
		candies int
		people  int
		expect  []int
	}{
		{1, 1, []int{1}},
		{0, 3, []int{0, 0, 0}},
		{13, 4, []int{4, 2, 3, 4}},
	}
	for _, tc := range tests {
		fmt.Printf("distribute %d to %d people: %v (%v)\n", tc.candies, tc.people, distributeCandies(tc.candies, tc.people), tc.expect)
	}
}
