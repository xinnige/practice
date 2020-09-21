package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCommonStrLength(t *testing.T) {
	tests := []struct {
		s1     string
		s2     string
		expect int
	}{
		{"asdfas", "werasdfaswer", 6},
		{"", "", 0},
		{"1", "2", 0},
		{"abc", "c", 1},
		{"b", "abc", 1},
		{"abc", "abc", 3},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, longestCommonStrLength(tc.s1, tc.s2))
	}
}
