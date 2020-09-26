package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCandy(t *testing.T) {
	tests := []struct {
		rates  []int
		expect int
	}{
		{[]int{}, 0},
		{[]int{3}, 1},
		{[]int{1, 0, 2}, 5},
		{[]int{1, 2, 2}, 4},
		{[]int{1, 0, 1, 2, 2, 3, 1, 4, 1}, 15},
		{[]int{1, 2, 87, 87, 87, 2, 1}, 13},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, candy(tc.rates))
	}

}
