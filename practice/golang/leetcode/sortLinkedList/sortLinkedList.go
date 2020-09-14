package main

import (
	"fmt"
)

type ListNode struct {
	Val int
    Next *ListNode
}

func merge(l *ListNode, r *ListNode) *ListNode {
    if l == nil {
        return r
    }
    if r == nil {
        return l
    }
    var p *ListNode
    if (l.Val < r.Val){
       p = l
       p.Next = merge(l.Next, r)
    } else {
	   p = r
       p.Next = merge(l, r.Next)
	}
    return p
}

func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
	}
    slow := head
	fast := head.Next
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
	}
    left := head
    right := slow.Next
    slow.Next = nil
    left = sortList(left)
    right = sortList(right)
	return merge(left, right)
}

func formatList(input []int) *ListNode {
    if len(input) == 0 {
        return nil
	}
	var tail *ListNode
    for i := len(input)-1; i >= 0; i-- {
        cnode := &ListNode{
           Val: input[i],
           Next: nil,
        }
        if tail != nil {
            cnode.Next = tail
		}
        tail = cnode
	}
    return tail
}

func printList(head *ListNode) {
	for head != nil {
        if head.Next == nil {
            fmt.Printf("%d", head.Val)
        } else {
		    fmt.Printf("%d -> ", head.Val)
		}
        head = head.Next
	}
    fmt.Println()
}

func main(){
    head := formatList([]int{6,9,3,-1,0,2,3,4})
    printList(head)
	head = sortList(head)
    printList(head)
}
