package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestQuickSort(t *testing.T) {

	testcases := []struct {
		input  []int
		expect []int
	}{
		// {[]int{16, 1, 0, 3, 10}, []int{0, 1, 3, 10, 16}},
		{[]int{9, 9, 4, 1}, []int{1, 4, 9, 9}},
	}
	for _, tc := range testcases {
		quickSort(tc.input, 0, len(tc.input)-1)
		assert.Equal(t, tc.expect, tc.input)
	}
}

func TestSortedSquares(t *testing.T) {

	testcases := []struct {
		input  []int
		expect []int
	}{
		{[]int{-4, -1, 0, 3, 10}, []int{0, 1, 9, 16, 100}},
		{[]int{-7, -3, 2, 3, 11}, []int{4, 9, 9, 49, 121}},
		{[]int{}, []int{}},
		{[]int{1}, []int{1}},
		{[]int{-3, -3, -2, 1}, []int{1, 4, 9, 9}},
	}
	for _, tc := range testcases {
		assert.Equal(t, tc.expect, sortedSquares(tc.input))
	}
}
