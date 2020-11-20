package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGenerateParenthesis(t *testing.T) {
	tests := []struct {
		input  int
		expect []string
	}{
		// {1, []string{"()"}},
		{2, []string{"()()", "((()))"}},
		// {3, []string{"()()()", "(()())", "((()))", "(())()", "()(())"}},
		// {4, []string{"(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"}},
	}
	for _, tc := range tests {
		assert.Equal(t, len(generateParenthesis(tc.input)), len(tc.expect))
	}
}
