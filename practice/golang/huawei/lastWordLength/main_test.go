package main

import (
	// "fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLastWordLength(t *testing.T) {
	tests := []struct {
		input  string
		expect int
	}{
		{"hello world", 5},
		{"", 0},
		{"hello", 5},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, lastWordLength(tc.input))
	}

}
