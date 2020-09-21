package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sroot := int(math.Sqrt(float64(n)))

	for i := 3; i <= sroot; i = i + 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func countPrimes(n int) int {
	if n == 0 || n == 1 {
		return 0
	}
	if n == 2 {
		return 0
	}
	if n == 3 || n == 4 {
		return n - 2
	}
	counter := 2
	for i := 5; i < n; i = i + 2 {
		if isPrime(i) {
			counter++
		}
	}
	return counter
}

func main() {
	tests := []struct {
		input  int
		expect int
	}{
		{10, 4},
		{0, 0},
		{1, 0},
		{2, 0},
		{3, 1},
		{4, 1},
		{5, 2},
		{25, 9},
	}
	for _, tc := range tests {
		fmt.Printf("expect count %d is %d == %d\n", tc.input, countPrimes(tc.input), tc.expect)
	}
}
