package main

import (
	"fmt"
)

func corpFlightBookings(bookings [][]int, n int) []int {
	seats := make([]int, n)
	for _, v := range bookings {
		seats[v[0]-1] += v[2]
		if v[1] < n {
			seats[v[1]] -= v[2]
		}
	}
	for i := 0; i < n-1; i++ {
		seats[i+1] += seats[i]
	}
	return seats
}

// func corpFlightBookings(bookings [][]int, n int) []int {
// 	seats := make([]int, n)
// 	for i := 0; i < len(bookings); i++ {
// 		for j := bookings[i][0] - 1; j < bookings[i][1]; j++ {
// 			seats[j] += bookings[i][2]
// 		}
// 	}
// 	return seats
// }

func main() {
	tests := []struct {
		bookings [][]int
		n        int
		expect   []int
	}{
		{[][]int{[]int{1, 2, 10}, []int{2, 3, 20}, []int{2, 5, 25}}, 5, []int{10, 55, 45, 25, 25}},
	}
	for _, tc := range tests {
		fmt.Printf("expects %v = %v\n", tc.expect, corpFlightBookings(tc.bookings, tc.n))
	}
}
