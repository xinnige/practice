package main

import (
	"fmt"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	carrier := 0
	var head, prev *ListNode
	var sum int
	if l1 == nil && l2 != nil {
		return l2
	}
	if l2 == nil && l1 != nil {
		return l1
	}
	if l1 == nil && l2 == nil {
		return head
	}

	for l1 != nil && l2 != nil {
		sum = l1.Val + l2.Val + carrier
		carrier = sum / 10
		lsum := &ListNode{Val: sum % 10}
		if prev == nil {
			head = lsum
			prev = lsum
		} else {
			prev.Next = lsum
			prev = prev.Next
		}
		l1 = l1.Next
		l2 = l2.Next
	}
	if l2 != nil {
		prev.Next = l2
	}
	if l1 != nil {
		prev.Next = l1
	}
	if prev.Next == nil {
		if carrier > 0 {
			prev.Next = &ListNode{Val: carrier}
		}
		return head
	}
	prev = prev.Next
	for prev.Next != nil {
		sum = prev.Val + carrier
		carrier = sum / 10
		prev.Val = sum % 10
		prev = prev.Next
	}
	sum = prev.Val + carrier
	if sum > 9 {
		prev.Val = sum % 10
		prev.Next = &ListNode{Val: sum / 10}
	} else {
		prev.Val = sum
	}
	return head
}

func printList(l *ListNode) {
	for l != nil && l.Next != nil {
		fmt.Printf("%d ->", l.Val)
		l = l.Next
	}
	fmt.Printf("%d\n", l.Val)
}

func construct(a []int) *ListNode {
	var h, p *ListNode
	for i := range a {
		if i == 0 {
			h = &ListNode{Val: a[i]}
			p = h
		} else {
			new := &ListNode{Val: a[i]}
			p.Next = new
			p = new
		}
	}
	return h
}

func main() {
	l1 := construct([]int{2, 4, 3})
	l2 := construct([]int{5, 6, 4})
	printList(l1)
	printList(l2)
	printList(addTwoNumbers(l1, l2))
}
