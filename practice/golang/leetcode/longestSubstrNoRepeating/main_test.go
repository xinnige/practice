package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestLengthOfLongestSubstring(t *testing.T) {
	testcases := []struct {
		input  string
		expect int
	}{
		{"bbbbb", 1},
		{"abcabcbb", 3},
		{"pwwkew", 3},
		{"", 0},
		{"a", 1},
		{"abcdefghjik", 11},
		{"aab", 2},
	}
	for _, tc := range testcases {
		assert.Equal(t, tc.expect, lengthOfLongestSubstring(tc.input))
	}
}
