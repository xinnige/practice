package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCorpFlightBookings(t *testing.T) {
	tests := []struct {
		bookings [][]int
		n        int
		expect   []int
	}{
		{[][]int{[]int{1, 2, 10}, []int{2, 3, 20}, []int{2, 5, 25}}, 5, []int{10, 55, 45, 25, 25}},
	}
	for _, tc := range tests {
		assert.Equal(t, tc.expect, corpFlightBookings(tc.bookings, tc.n))
	}
}
