package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func convert(l *ListNode) []int {
	ret := make([]int, 0)
	for l != nil {
		ret = append(ret, l.Val)
		l = l.Next
	}
	return ret
}

func TestAddTwoNumbers(t *testing.T) {
	testcases := []struct {
		num1   []int
		num2   []int
		expect []int
	}{
		{[]int{}, []int{}, []int{}},
		{[]int{1}, []int{}, []int{1}},
		{[]int{1}, []int{9}, []int{0, 1}},
		{[]int{1, 2, 3, 4}, []int{}, []int{1, 2, 3, 4}},
		{[]int{}, []int{1, 2, 3, 4}, []int{1, 2, 3, 4}},
		{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
		{[]int{1}, []int{1, 1}, []int{2, 1}},
		{[]int{1, 2}, []int{3}, []int{4, 2}},
		{[]int{1, 9}, []int{9}, []int{0, 0, 1}},
		{[]int{1}, []int{9, 9, 9, 9}, []int{0, 0, 0, 0, 1}},
		{[]int{9, 9, 9, 9}, []int{1}, []int{0, 0, 0, 0, 1}},
		{[]int{9, 9, 9, 9}, []int{9}, []int{8, 0, 0, 0, 1}},
		{[]int{9, 8}, []int{1}, []int{0, 9}},
	}

	for _, tc := range testcases {
		l1 := construct(tc.num1)
		l2 := construct(tc.num2)
		l3 := addTwoNumbers(l1, l2)
		assert.Equal(t, tc.expect, convert(l3))
	}
}
