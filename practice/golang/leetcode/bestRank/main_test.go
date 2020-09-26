package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestScores(t *testing.T) {
	tests := []struct {
		scores    [][]int
		countries []int
		expect    [][]int
	}{
		{
			[][]int{[]int{51, 100, 1000}, []int{36, 110, 300}, []int{6, 14, 32}, []int{5, 18, 40}},
			[]int{0, 1, 2, 3},
			[][]int{[]int{1, 1}, []int{1, 2}, []int{1, 3}, []int{1, 4}},
		},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expect, rank(tc.scores, tc.countries))
	}
}
