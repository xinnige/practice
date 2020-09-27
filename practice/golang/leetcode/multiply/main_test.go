package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMultiply(t *testing.T) {
	tests := []struct {
		num1   string
		num2   string
		expect string
	}{
		{"0", "9999", "0"},
		{"2", "3", "6"},
		{"12", "8", "96"},
		{"123", "456", "56088"},
		{"9999", "999", "9989001"},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, multiply(tc.num1, tc.num2))
	}
}
