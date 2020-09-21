package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCodeString(t *testing.T) {
	tests := []struct {
		input  string
		expect string
	}{
		{"AAAABCCDAA", "4A1B2C1D2A"},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, codeString(tc.input))
	}
}
