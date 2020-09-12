package main

import (
	"fmt"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	nums := make([]int, len(nums1)+len(nums2))
	i, j := 0, 0
	for i < len(nums1) && j < len(nums2) {
		if nums1[i] <= nums2[j] {
			nums[i+j] = nums1[i]
			i++
		} else {
			nums[i+j] = nums2[j]
			j++
		}
	}
	for ; i < len(nums1); i++ {
		nums[i+j] = nums1[i]
	}
	for ; j < len(nums2); j++ {
		nums[i+j] = nums2[j]
	}
	fmt.Printf("%v\n", nums)
	if len(nums) == 0 {
		return 0
	}
	if len(nums)%2 == 1 {
		return float64(nums[len(nums)/2])
	}
	return float64(nums[(len(nums)-1)/2]+nums[len(nums)/2]) / 2
}

func main() {
	testcases := []struct {
		nums1  []int
		nums2  []int
		expect float64
	}{
		// {[]int{1, 4, 5, 7, 8}, []int{0, 2, 4, 6, 8, 9}, 5},
		{[]int{1, 3}, []int{2}, 2},
	}
	for _, tc := range testcases {
		fmt.Printf("%f=%f\n", tc.expect, findMedianSortedArrays(tc.nums1, tc.nums2))
	}
}
