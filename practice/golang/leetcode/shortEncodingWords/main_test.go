package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMinimumLengthEncoding(t *testing.T) {
	tests := []struct {
		words  []string
		expect int
	}{
		{[]string{"time", "me", "bell"}, 10},
		{[]string{"time", "me", "bell", "im"}, 13},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, minimumLengthEncoding(tc.words))
	}
}
