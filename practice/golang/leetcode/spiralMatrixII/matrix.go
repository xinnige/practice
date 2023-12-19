package main

func generateMatrix(n int) [][]int {
	if n == 0 {
		return [][]int{}
	}
	matrix := make([][]int, n)
	for i := 0; i < n; i++ {
		matrix[i] = make([]int, n)
	}

	size := n - 1
	rowCursor := 0
	colCursor := 0
	num := 1
	max := n * n

	rowBuoy := size
	colBuoy := size

	for rowCursor <= rowBuoy && colCursor <= colBuoy {
		for i := colCursor; i <= colBuoy && num <= max; i++ {
			matrix[rowCursor][i] = num
			num++
		}
		rowCursor++
		for i := rowCursor; i <= rowBuoy && num <= max; i++ {
			matrix[i][colBuoy] = num
			num++
		}
		colBuoy--
		for i := colBuoy; i >= colCursor && num <= max; i-- {
			matrix[rowBuoy][i] = num
			num++
		}
		rowBuoy--
		for i := rowBuoy; i >= rowCursor && num <= max; i-- {
			matrix[i][colCursor] = num
			num++
		}
		colCursor++
	}
	return matrix
}
