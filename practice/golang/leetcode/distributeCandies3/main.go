package main

import (
	"fmt"
)

func candy(ratings []int) int {
	candies := make([]int, len(ratings))
	if len(ratings) == 0 || len(ratings) == 1 {
		return len(ratings)
	}
	cnt := 0
	for cnt < len(candies) {
		for i := range ratings {
			if i == 0 {
				if ratings[i] > ratings[i+1] {
					if candies[i] == 0 && candies[i+1] != 0 {
						candies[i] += candies[i+1] + 1
						cnt++
					}
				} else {
					if candies[i] == 0 {
						candies[i] = 1
						cnt++
					}
				}
			} else if i == len(ratings)-1 {
				if ratings[i] > ratings[i-1] {
					if candies[i] == 0 && candies[i-1] != 0 {
						candies[i] += candies[i-1] + 1
						cnt++
					}
				} else {
					if candies[i] == 0 {
						candies[i] = 1
						cnt++
					}
				}

			} else {
				if ratings[i] > ratings[i-1] && ratings[i] > ratings[i+1] {
					if candies[i] == 0 && candies[i-1] != 0 && candies[i+1] != 0 {
						if candies[i-1] > candies[i+1] {
							candies[i] += candies[i-1] + 1
						} else {
							candies[i] += candies[i+1] + 1
						}
						cnt++
					}
				} else if ratings[i] <= ratings[i+1] && ratings[i] > ratings[i-1] {
					if candies[i] == 0 && candies[i-1] != 0 {
						candies[i] += candies[i-1] + 1
						cnt++
					}
				} else if ratings[i] <= ratings[i-1] && ratings[i] > ratings[i+1] {
					if candies[i] == 0 && candies[i+1] != 0 {
						candies[i] += candies[i+1] + 1
						cnt++
					}
				} else {
					if candies[i] == 0 {
						candies[i] = 1
						cnt++
					}
				}
			}
		}
	}
	fmt.Printf("%v\n", candies)
	sum := 0
	for _, v := range candies {
		sum += v
	}
	return sum
}

func main() {
	tests := []struct {
		rates  []int
		expect int
	}{
		{[]int{}, 0},
		{[]int{3}, 1},
		{[]int{1, 0, 2}, 5},
		{[]int{1, 2, 2}, 4},
		{[]int{1, 0, 1, 2, 2, 3, 1, 4, 1}, 15},
	}
	for _, tc := range tests {
		fmt.Printf("%v -> %d (expects %d)\n", tc.rates, candy(tc.rates), tc.expect)
	}
}
