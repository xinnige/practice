package main

import (
	"fmt"
)

func bubbleSort(numbers []int) {
	for i := 0; i < len(numbers)-1; i++ {
		for j := 0; j < len(numbers)-1-i; j++ {
			if numbers[j] > numbers[j+1] {
				numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
			}
		}
	}
}

func main() {
	tests := []struct {
		input  []int
		expect []int
	}{
		{[]int{32, 5, 3, 6, 7, 54, 87}, []int{}},
	}

	for _, tc := range tests {
		fmt.Printf("%v -> ", tc.input)
		bubbleSort(tc.input)
		fmt.Printf("%v\n", tc.input)
	}
}
