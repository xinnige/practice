package main

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestMyAtoi(t *testing.T) {
	tests := []struct {
		input  string
		expect int
	}{
		{"42", 42},
		{"00000000042", 42},
		{"       42  aaaaa", 42},
		{"     00-42", 0},
		{"-91283472332", -2147483648},
		{"9223372036854775808", 2147483647},
		{"18446744073709551617", 2147483647},
	}

	for _, tc := range tests {
		require.Equal(t, tc.expect, myAtoi(tc.input))
	}
}
