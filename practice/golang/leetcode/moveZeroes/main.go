package main

import (
    "fmt"
)


func moveZeroes(nums []int){

    counter := 0
    var tmp int
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            fmt.Printf("%d <-> %d\n", counter, i)
            tmp = nums[counter]
            nums[counter] = nums[i]
            nums[i] = tmp
            counter++
        }
        fmt.Printf("%v\n", nums)
    }
}

// func moveZeroes(nums []int){
//     counter := 0
//     for i:=0; i< len(nums); i++ {
//         if nums[i] == 0 {
//             counter++
//         } else {
//             if counter != 0 {
//                 nums[i-counter] = nums[i]
//             }
//         }
        
//     }
//     for i:=len(nums)-counter; i<len(nums); i++ {
//         nums[i] = 0
//     }
// }

func main(){
    testcases := [][]int{
        // []int{0,0,0},
        []int{0,1,2,3,0,4,0,5},
        // []int{0,1,0,3,12},
        // []int{1},
        // []int{},
        // []int{0},
        // []int{1,2,3,4,5,6},
    }
    for _, tc := range testcases {
        fmt.Printf("%v -> ", tc)
        moveZeroes(tc)
        fmt.Printf("%v\n", tc)
    }
}
