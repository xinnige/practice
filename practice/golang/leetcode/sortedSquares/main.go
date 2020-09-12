package main

import (
	"fmt"
)

func quickSort(A []int) {
	if len(A) <= 1 {
		return
	}
	p := A[0]
	i, j := 1, len(A)-1
	for i < j {
		for A[j] > p && i < j {
			j--
		}
		for A[i] <= p && i < j {
			i++
		}
		tmp := A[i]
		A[i] = A[j]
		A[j] = tmp
	}
	if A[i] > p {
		A[0] = A[i-1]
		A[i-1] = p
	} else {
		A[0] = A[i]
		A[i] = p
	}
	if i > 1 {
		quickSort(A[0:i])
	}
	if i < len(A)-1 {
		quickSort(A[i:])
	}
}

func sortedSquares(A []int) []int {
	if len(A) == 0 {
		return A
	}
	for i := range A {
		A[i] = A[i] * A[i]
	}
	quickSort(A, 0, len(A)-1)
	return A
}

func main() {

	testcases := [][]int{
		[]int{-4, -1, 0, 3, 10},
		// []int{},
		// []int{},
	}
	for _, tc := range testcases {
		fmt.Printf("%v\n", sortedSquares(tc))
	}
}
