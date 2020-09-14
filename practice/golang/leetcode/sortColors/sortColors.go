package main

import (
	"fmt"
)

func sortColors(nums []int)  {
    if len(nums) == 0 {
        return
    }
    counter := map[int]int{0:0,1:0,2:0}

    for i := range nums {
        counter[nums[i]] = counter[nums[i]] + 1
    }
    // fmt.Printf("counter: %v\n", counter)
    color := 0
    c := 0
    for i := 0; i < len(nums); {
        // fmt.Printf("color=%d, c=%d\n", color, c)
        if c >=  counter[color] {
            color = color + 1
            c = 0
            // fmt.Printf("%v\n", nums)
            continue
		}
        nums[i] = color
        c = c + 1
        i = i + 1
        // fmt.Printf("%v\n", nums)
	}
}

func main() {
    inputs :=  [][]int{
		{2,0,2,1,1,0},
		{2},
        {},
		{2,0,2,1,1,0,0,1,1,1,2,2,2},
	}

    for _, input := range inputs {
        fmt.Printf("%v\n", input)
        sortColors(input)
        fmt.Printf("%v\n", input)
	}
}
