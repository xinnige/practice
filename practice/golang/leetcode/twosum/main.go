package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	for i := range nums {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func main() {
	input := []int{2, 7, 11, 15}
	target := 9
	fmt.Printf("%v, %d, %v", input, target, twoSum(input, target))
}
