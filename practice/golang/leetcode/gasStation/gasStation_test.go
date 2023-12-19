package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestCanCompleteCircuit(t *testing.T) {

	tests := []struct {
		gas    []int
		cost   []int
		expect int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{3, 4, 5, 1, 2}, 3},
		{[]int{2, 3, 4}, []int{3, 4, 3}, -1},
		{[]int{3, 1, 1}, []int{1, 2, 2}, 0},
		{[]int{0, 0, 0, 0, 0, 0, 0, 0, 2}, []int{0, 0, 0, 0, 0, 0, 0, 1, 0}, 8},
		{[]int{5, 8, 2, 8}, []int{6, 5, 6, 6}, 3},
		{[]int{2, 0, 0, 0, 0, 0, 0, 0, 0}, []int{0, 1, 0, 0, 0, 0, 0, 0, 0}, 0},
	}
	for _, tc := range tests {
		require.Equal(t, tc.expect, canCompleteCircuit(tc.gas, tc.cost))

	}
}
