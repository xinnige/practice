package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestGenerateMatrix(t *testing.T) {
	tests := []struct {
		input  int
		expect [][]int
	}{
		{0, [][]int{}},
		{1, [][]int{{1}}},
		{2, [][]int{{1, 2}, {4, 3}}},
		{3, [][]int{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}},
		{4, [][]int{{1, 2, 3, 4}, {12, 13, 14, 5}, {11, 16, 15, 6}, {10, 9, 8, 7}}},
	}

	for _, tc := range tests {
		matrix := generateMatrix(tc.input)
		require.Equal(t, tc.expect, matrix)
	}

}
