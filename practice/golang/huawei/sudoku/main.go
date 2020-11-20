package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func getCandidate(suji [][]int, row, col int) []int {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	ridx := (row / 3) * 3
	cidx := (col / 3) * 3
	for c := 0; c < 9; c++ {
		// row
		for i := 0; i < 9; i++ {
			if suji[row][i] == numbers[c] {
				numbers[c] = -1
				continue
			}
		}
		// col
		for i := 0; i < 9; i++ {
			if suji[i][col] == numbers[c] {
				numbers[c] = -1
				continue
			}
		}
		// lean
		for i := 0; i < 3; i++ {
			for j := 0; j < 3; j++ {
				if suji[ridx+i][cidx+j] == numbers[c] {
					numbers[c] = -1
					continue
				}
			}
		}
	}
	candidate := make([]int, 0)
	for _, c := range numbers {
		if c != -1 {
			candidate = append(candidate, c)
		}
	}
	return candidate

}

func fill(suji [][]int, row, col int) bool {
	candidate := getCandidate(suji, row, col)
	if len(candidate) == 0 {
		return false
	}
	for _, c := range candidate {
		suji[row][col] = c
		if sudokuFill(suji, row, col+1) {
			return true
		}
	}
	return false
}

func sudokuFill(suji [][]int, r, c int) bool {
	for i := r; i < 9; i++ {
		for j := c; j < 9; j++ {
			if suji[i][j] == 0 {
				if !fill(suji, i, j) {
					return false
				}
			}
		}
	}
	return true
}

func sudoku(suji [][]int) {
	sudokuFill(suji, 0, 0)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	input := make([][]int, 9)

	for i := 0; i < 9; i++ {
		scanner.Scan()
		s := scanner.Text()
		row := make([]int, 9)
		for j := 0; j < 9; j++ {
			n, _ := strconv.Atoi(string(s[j]))
			row[j] = n
		}
		input[i] = row
	}
	sudoku(input)

	for i := 0; i < 9; i++ {
		fmt.Printf("%v\n", input[i])
	}

}
