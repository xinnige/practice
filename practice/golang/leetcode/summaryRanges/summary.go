package main

import "fmt"

func summaryRanges(nums []int) []string {
	if len(nums) == 1 {
		return []string{fmt.Sprintf("%d", nums[0])}
	}

	result := make([]string, 0)
	var i, start, end int
	for i = 0; i < len(nums)-1; i++ {
		start = nums[i]
		for (i < len(nums)-1) && (nums[i+1] == nums[i]+1) {
			i++
		}
		end = nums[i]
		if start == end {
			result = append(result, fmt.Sprintf("%d", start))
		} else {
			result = append(result, fmt.Sprintf("%d->%d", start, end))
		}
	}
	if i == len(nums) {
		return result
	}
	// last one
	if end+1 == nums[len(nums)-1] {
		result[len(result)-1] = fmt.Sprintf("%d->%d", start, end+1)
	} else {
		result = append(result, fmt.Sprintf("%d", nums[len(nums)-1]))
	}
	return result
}
