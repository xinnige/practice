package main

import (
	// "fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCountPrime(t *testing.T) {
	tests := []struct {
		input  int
		expect int
	}{
		{10, 4},
		{0, 0},
		{1, 0},
		{2, 0},
		{3, 1},
		{4, 2},
		{5, 2},
		{25, 9},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expect, countPrimes(tc.input))
	}
}

func TestIsPrime(t *testing.T) {
	tests := []struct {
		input  int
		expect bool
	}{
		{2, true},
		{3, true},
		{4, false},
		{5, true},
		{6, false},
		{7, true},
		{9, false},
		{11, true},
		{13, true},
		{17, true},
		{19, true},
		{23, true},
		{25, false},
	}

	for _, tc := range tests {
		assert.Equal(t, tc.expect, isPrime(tc.input))
	}
}
