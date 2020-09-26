package main

import (
	"fmt"
)

func swap(n []int, i int) {
	tmp := n[i]
	n[i] = n[0]
	n[0] = tmp
}

func permute(n []int) [][]int {
	if len(n) == 1 {
		return [][]int{n}
	}
	if len(n) == 2 {
		return [][]int{[]int{n[0], n[1]}, []int{n[1], n[0]}}
	}
	ret := make([][]int, 0)
	pswaps := permute(n[1:])
	for _, v := range pswaps {
		ret = append(ret, append([]int{n[0]}, v...))
	}
	for i := 1; i < len(n); i++ {
		swap(n, i)
		pswaps = permute(n[1:])
		for _, v := range pswaps {
			ret = append(ret, append([]int{n[0]}, v...))
		}
		swap(n, i)
	}
	return ret
}

func permuteLength(nums []int) int {
	return len(permute(nums))
}

func main() {
	// fmt.Printf("%v\n", permute([]int{1}))
	// fmt.Printf("%v\n", permute([]int{1, 2}))
	// fmt.Printf("%v\n", permute([]int{1, 2, 3}))
	fmt.Printf("%v\n", permute([]int{1, 2, 3, 4}))
}
