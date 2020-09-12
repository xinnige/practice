package main

import (
	"fmt"
)

func merge(nums1 []int, m int, nums2 []int, n int) {
	t := m + n - 1
	i, j := m-1, n-1
	for i >= 0 && j >= 0 {
		if nums1[i] <= nums2[j] {
			nums1[t] = nums2[j]
			j--
		} else {
			nums1[t] = nums1[i]
			i--
		}
		t--
	}
	for ; j >= 0; j-- {
		nums1[t] = nums2[j]
		t--
	}
}

func main() {
	testcases := []struct {
		nums1 []int
		nums2 []int
		m     int
		n     int
	}{
		// {[]int{1, 4, 5, 7, 8}, []int{0, 2, 4, 6, 8, 9}, 5},
		{[]int{1, 3, 0}, []int{2}, 2, 1},
		{[]int{1, 4, 5, 7, 8, 0, 0, 0, 0, 0, 0}, []int{0, 2, 4, 6, 8, 9}, 5, 6},
		{[]int{}, []int{}, 0, 0},
		{[]int{1, 0}, []int{2}, 1, 1},
		{[]int{1, 3, 0}, []int{2}, 2, 1},
		{[]int{0, 0, 0}, []int{0}, 2, 1},
		{[]int{1}, []int{}, 1, 0},
		{[]int{0}, []int{2}, 0, 1},
	}
	for _, tc := range testcases {
		merge(tc.nums1, tc.m, tc.nums2, tc.n)
		fmt.Printf("%v\n", tc.nums1)
	}
}
