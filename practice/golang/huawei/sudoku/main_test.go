package main

import (
	// "fmt"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestSudoku(t *testing.T) {
	tests := []struct {
		input  [][]int
		expect [][]int
	}{
		{
			[][]int{
				[]int{0, 9, 2, 4, 8, 1, 0, 6, 3},
				[]int{4, 1, 3, 7, 6, 2, 9, 8, 5},
				[]int{8, 6, 0, 3, 5, 9, 4, 1, 2},
				[]int{6, 2, 4, 1, 9, 5, 3, 7, 8},
				[]int{7, 5, 9, 8, 4, 3, 1, 2, 6},
				[]int{1, 3, 8, 6, 2, 7, 5, 9, 4},
				[]int{2, 7, 1, 5, 3, 8, 6, 4, 9},
				[]int{3, 8, 6, 9, 1, 4, 2, 5, 7},
				[]int{0, 4, 5, 2, 7, 6, 8, 3, 1},
			}, [][]int{
				[]int{5, 9, 2, 4, 8, 1, 7, 6, 3},
				[]int{4, 1, 3, 7, 6, 2, 9, 8, 5},
				[]int{8, 6, 7, 3, 5, 9, 4, 1, 2},
				[]int{6, 2, 4, 1, 9, 5, 3, 7, 8},
				[]int{7, 5, 9, 8, 4, 3, 1, 2, 6},
				[]int{1, 3, 8, 6, 2, 7, 5, 9, 4},
				[]int{2, 7, 1, 5, 3, 8, 6, 4, 9},
				[]int{3, 8, 6, 9, 1, 4, 2, 5, 7},
				[]int{9, 4, 5, 2, 7, 6, 8, 3, 1},
			}},
		{
			[][]int{
				[]int{5, 3, 0, 0, 7, 0, 0, 0, 0},
				[]int{6, 0, 0, 1, 9, 5, 0, 0, 0},
				[]int{0, 9, 8, 0, 0, 0, 0, 6, 0},
				[]int{8, 0, 0, 0, 6, 0, 0, 0, 3},
				[]int{4, 0, 0, 8, 0, 3, 0, 0, 1},
				[]int{7, 0, 0, 0, 2, 0, 0, 0, 6},
				[]int{0, 6, 0, 0, 0, 0, 2, 8, 0},
				[]int{0, 0, 0, 4, 1, 9, 0, 0, 5},
				[]int{0, 0, 0, 0, 8, 0, 0, 7, 9},
			},
			[][]int{
				[]int{5, 3, 4, 6, 7, 8, 9, 1, 2},
				[]int{6, 7, 2, 1, 9, 5, 3, 4, 8},
				[]int{1, 9, 8, 3, 4, 2, 5, 6, 7},
				[]int{8, 5, 9, 7, 6, 1, 4, 2, 3},
				[]int{4, 2, 6, 8, 5, 3, 7, 9, 1},
				[]int{7, 1, 3, 9, 2, 4, 8, 5, 6},
				[]int{9, 6, 1, 5, 3, 7, 2, 8, 4},
				[]int{2, 8, 7, 4, 1, 9, 6, 3, 5},
				[]int{3, 4, 5, 2, 8, 6, 1, 7, 9},
			},
		},
	}

	for _, tc := range tests {
		sudoku(tc.input)
		assert.Equal(t, tc.expect, tc.input)
	}
}