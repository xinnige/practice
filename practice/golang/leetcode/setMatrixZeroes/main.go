package main

import (
	"fmt"
)

func isTopZero(matrix[][]int) bool {
    for j := range matrix[0] {
        if matrix[0][j] == 0 {
            return true
        }
    }
    return false
}
func isLeftZero(matrix[][]int) bool {
    for i := range matrix {
        if matrix[i][0] == 0 {
            return true
        }
    }
    return false
}

func setZeroes(matrix [][]int)  {
    if len(matrix) == 0 {
        return
    }
    if len(matrix[0]) == 0 {
        return
    }
    topZero := isTopZero(matrix)
    leftZero := isLeftZero(matrix)

    for ridx := range matrix {
      for cidx := range  matrix[ridx] {
		if matrix[ridx][cidx] == 0{
            matrix[ridx][0] = 0
            matrix[0][cidx] = 0
        }
      }
    }
    // fmt.Printf("%v\n", matrix)
    for i := 1; i < len(matrix); i++ {
        if matrix[i][0] == 0 {
            for j := range matrix[i] {
                matrix[i][j] = 0
            }
        }
    }
    for j := 1; j < len(matrix[0]); j++ {
       if matrix[0][j] == 0 {
            for i := range matrix {
                matrix[i][j] = 0
            }
       }
    }
    if leftZero {
        for i := range matrix {
            matrix[i][0] = 0
        }
    }
    if topZero {
        for j := range matrix[0] {
            matrix[0][j] = 0
        }
    }
}

func main(){
        // matrix := [][]int{[]int{0,1,2,0}, []int{3,4,5,2}, []int{1,3,1,5}}
        // matrix := [][]int{[]int{1,2,3,4},[]int{5,0,7,8},[]int{0,10,11,12},[]int{13,14,15,0}}

        matrix := [][]int{[]int{1,0,3}}
        fmt.Printf("%v\n", matrix)
        setZeroes(matrix)
        fmt.Printf("%v\n", matrix)

}
