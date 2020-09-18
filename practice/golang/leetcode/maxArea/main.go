package main

import (
	"fmt"
)

func min(a,b int) int{
	if a < b {
		return a
	}
	return b
}

func maxArea(height []int) int {
	i, j := 0, len(height) -1
	maxVol := 0
	
	for (i < j) {
		vol := min(height[i], height[j]) * (j-i)
		if maxVol < vol {
			maxVol = vol
		}
		if (height[i] < height[j]){
			i++
		} else {
			j--
		}
	}
	return maxVol
}

// func maxArea(height []int) int {
// 	maxVol := 0
//     for i := range height {
// 		for j := i; j < len(height); j++ {
// 			volume := min(height[i], height[j]) * (j-i)
// 			if volume > maxVol {
// 				maxVol = volume 
// 			}
// 		}
// 	}
// 	return maxVol
// }

func main(){
	tests := []struct{
		input []int
		expect int
	}{
		{[]int{1,8,6,2,5,4,8,3,7}, 49},
		{[]int{1,1}, 1},
		{[]int{1,1,1}, 2},
		{[]int{2,3,10,5,7,8,9}, 36},
	}

	for _, tc := range tests {
		fmt.Printf("%d=%d\n", tc.expect, maxArea(tc.input))
	}
}