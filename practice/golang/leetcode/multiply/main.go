package main

import (
	"fmt"
	"strconv"
)

func atoi(num1 string) []int {
	nlen := len(num1)
	number := make([]int, nlen)

	for i, c := range num1 {
		number[nlen-i-1], _ = strconv.Atoi(string(c))
	}
	return number
}

func adds(sums [][]int, nlen int) []int {
	mul := make([]int, nlen)
	var sum, c int
	for i := 0; i < nlen; i++ {
		for j := range sums {
			sum += sums[j][i]
		}
		mul[i] = (sum + c) % 10
		c = (sum + c) / 10
		sum = 0
	}
	return mul
}

func reverse(digits []int) string {
	nlen := len(digits)
	number := make([]byte, nlen)
	for i := range digits {
		number[nlen-i-1] = []byte(fmt.Sprintf("%d", digits[i]))[0]
	}
	if digits[nlen-1] == 0 {
		return string(number[1:])
	}
	return string(number)
}

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	sums := make([][]int, len(num1))
	n1 := atoi(num1)
	n2 := atoi(num2)
	var carrier int
	for i := range n1 {
		carrier = 0
		sums[i] = make([]int, len(num1)+len(num2))
		for j := range n2 {
			m := n1[i]*n2[j] + carrier
			carrier = m / 10
			sums[i][j+i] = m % 10
		}
		sums[i][i+len(num2)] = carrier
	}

	// adds sums
	mul := adds(sums, len(num1)+len(num2))

	// reverse and remove initial 0
	return reverse(mul)
}

func main() {
	tests := []struct {
		num1   string
		num2   string
		expect string
	}{
		{"2", "3", "6"},
		{"123", "456", "56088"},
	}
	for _, tc := range tests {
		fmt.Printf("%s x %s = %s (expects %s)", tc.num1, tc.num2, multiply(tc.num1, tc.num2), tc.expect)
	}
}
