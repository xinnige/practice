package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGetMinDp(t *testing.T) {
	tests := []struct {
		input  [][]int
		expect []int
	}{
		{
			[][]int{[]int{1, 2}, []int{2, 3}, []int{3, 4}, []int{4, 5}},
			[]int{3},
		},
		{
			[][]int{[]int{1, 2}, []int{2, 3}, []int{2, 5}, []int{3, 4}, []int{3, 6}},
			[]int{2, 3},
		},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, getMinDp(tc.input))
	}
}
