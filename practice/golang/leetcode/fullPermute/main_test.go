package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPermute(t *testing.T) {
	testcases := []struct {
		input  []int
		expect int
	}{
		{[]int{1, 2, 3}, 6},
		{[]int{1, 2, 3, 4}, 24},
	}
	for _, tc := range testcases {
		assert.Equal(t, tc.expect, permuteLength(tc.input))
	}
}
