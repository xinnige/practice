package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestFindMediumSortedArray(t *testing.T) {

	testcases := []struct {
		nums1  []int
		nums2  []int
		expect float64
	}{
		{[]int{1, 4, 5, 7, 8}, []int{0, 2, 4, 6, 8, 9}, 5},
		{[]int{}, []int{}, 0},
		{[]int{1}, []int{2}, 1.5},
		{[]int{1, 3}, []int{2}, 2},
		{[]int{0, 0}, []int{0}, 0},
		{[]int{1}, []int{}, 1},
		{[]int{}, []int{2}, 2},
	}
	for _, tc := range testcases {
		assert.Equal(t, tc.expect, findMedianSortedArrays(tc.nums1, tc.nums2))
	}
}
