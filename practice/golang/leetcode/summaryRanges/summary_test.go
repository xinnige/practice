package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestSummary(t *testing.T) {
	tests := []struct {
		input  []int
		expect []string
	}{
		{[]int{0}, []string{"0"}},
		{[]int{1}, []string{"1"}},
		// {[]int{0, 2, 3, 4, 6, 8, 9}, []string{"0", "2->4", "6", "8->9"}},
		// {[]int{0, 1, 2, 4, 5, 7}, []string{"0->2", "4->5", "7"}},
		// {[]int{0, 1, 2, 3, 4, 5}, []string{"0->5"}},
		// {[]int{0, 2, 4, 6}, []string{"0", "2", "4", "6"}},
	}

	for _, tc := range tests {
		require.Equal(t, tc.expect, summaryRanges(tc.input))
	}
}
