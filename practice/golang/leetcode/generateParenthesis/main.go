package main

import (
	"fmt"
)

func generateParenthesis(n int) []string {
	res := make([]string, 0)
	backtrack(n, n, &res, "")
	return res
}

func backtrack(left, right int, res *[]string, cur string) {
	if left == 0 && right == 0 {
		*res = append(*res, cur)
		return
	}

	if right < left {
		return
	}

	if left > 0 {
		backtrack(left-1, right, res, cur+"(")
	}

	if right > 0 {
		backtrack(left, right-1, res, cur+")")
	}
}

func main() {
	tests := []struct {
		input  int
		expect []string
	}{
		{2, []string{"()()", "((()))"}},
		{3, []string{"()()()", "(()())", "((()))", "(())()", "()(())"}},
		{4, []string{"()()()()", "(()()())", "(()())()", "()(()())", "(((())))", "()((()))", "((()))()", "((())())", "((())())", "(()(()))"}},
	}
	for _, tc := range tests {
		fmt.Printf("%d -> %v\n(expects %v)\n", tc.input, generateParenthesis(tc.input), tc.expect)
	}
}
