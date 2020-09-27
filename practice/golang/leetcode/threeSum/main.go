package main

import (
	"fmt"
	"sort"
)

func threeSum(nums []int) [][]int {
	ret := make([][]int, 0)
	nlen := len(nums)
	if nlen < 3 {
		return ret
	}
	sort.Ints(nums)

	for i := 0; i < nlen-2; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		low, high, sum := i+1, nlen-1, 0-nums[i]
		for low < high {
			if nums[low]+nums[high] == sum {
				ret = append(ret, []int{nums[i], nums[low], nums[high]})
				for low < high && nums[low] == nums[low+1] {
					low++
				}
				for low < high && nums[high] == nums[high-1] {
					high--
				}
				low++
				high--
			} else if nums[low]+nums[high] > sum {
				high--
			} else {
				low++
			}
		}
	}
	return ret
}

func main() {
	tests := []struct {
		input  []int
		expect [][]int
	}{
		{[]int{-1, 0, 1, 2, -1, -4}, [][]int{[]int{1, -1, 2}, []int{-1, 0, 1}}},
		{[]int{0}, [][]int{}},
		{
			[]int{-13, 5, 13, 12, -2, -11, -1, 12, -3, 0, -3, -7, -7, -5, -3, -15, -2, 14, 14, 13, 6, -11, -11, 5, -15, -14, 5, -5, -2, 0, 3, -8, -10, -7, 11, -5, -10, -5, -7, -6, 2, 5, 3, 2, 7, 7, 3, -10, -2, 2, -12, -11, -1, 14, 10, -9, -15, -8, -7, -9, 7, 3, -2, 5, 11, -13, -15, 8, -3, -7, -12, 7, 5, -2, -6, -3, -10, 4, 2, -5, 14, -3, -1, -10, -3, -14, -4, -3, -7, -4, 3, 8, 14, 9, -2, 10, 11, -10, -4, -15, -9, -1, -1, 3, 4, 1, 8, 1},
			[][]int{},
		},
	}

	for _, tc := range tests {
		fmt.Printf("threeSum 0 of %v is %v (expects %v)\n", tc.input, threeSum(tc.input), tc.expect)
	}
}
