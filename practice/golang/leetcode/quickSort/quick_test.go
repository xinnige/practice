package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestQuickSort(t *testing.T) {
	tests := []struct {
		input  []int
		expect []int
	}{
		// {[]int{2, 1}, []int{1, 2}},
		// {[]int{0, -1, -2}, []int{-2, -1, 0}},
		// {[]int{8, 9, 3, 1, 3, 8, 3, 1, 2, 4, 9, 5, 7, 2}, []int{1, 1, 2, 2, 3, 3, 3, 4, 5, 7, 8, 8, 9, 9}},
		{[]int{8, 9, 3, 1, 2, 4, 5, 7}, []int{1, 2, 3, 4, 5, 7, 8, 9}},
	}

	for _, tc := range tests {
		quickSort2(tc.input, 0, len(tc.input)-1)
		assert.Equal(t, tc.expect, tc.input)
	}

}
