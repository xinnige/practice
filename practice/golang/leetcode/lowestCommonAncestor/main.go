package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil || root == p || root == q {
		return root
	}
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left != nil {
		return left
	}
	return right
}

func connectNodes(root *TreeNode, idx int, nodes []int) {
	if idx*2+1 >= len(nodes) {
		return
	}
	if nodes[idx*2+1] != -1 {
		root.Left = &TreeNode{Val: nodes[idx*2+1]}
		connectNodes(root.Left, idx*2+1, nodes)
	}
	if idx*2+2 >= len(nodes) {
		return
	}
	if nodes[idx*2+2] != -1 {
		root.Right = &TreeNode{Val: nodes[idx*2+2]}
		connectNodes(root.Right, idx*2+2, nodes)
	}
}

func formatTree(nodes []int) *TreeNode {
	if len(nodes) == 0 {
		return nil
	}
	root := &TreeNode{Val: nodes[0]}
	connectNodes(root, 0, nodes)
	return root
}

func printTreeDfs(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Printf("%d ", root.Val)
	if root.Left != nil {
		printTreeDfs(root.Left)
	}
	if root.Right != nil {
		printTreeDfs(root.Right)
	}
}

func searchTreeNode(root *TreeNode, v int) *TreeNode {
	if root.Val == v {
		return root
	}
	var node *TreeNode
	if root.Left != nil {
		node = searchTreeNode(root.Left, v)
	}
	if node != nil {
		return node
	}
	if root.Right != nil {
		node = searchTreeNode(root.Right, v)
	}
	return node
}

func main() {
	tests := []struct {
		nodes []int
		p     int
		q     int
	}{
		{[]int{3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4}, 5, 1},
	}

	for _, tc := range tests {
		root := formatTree(tc.nodes)
		p := searchTreeNode(root, tc.p)
		q := searchTreeNode(root, tc.q)
		lca := lowestCommonAncestor(root, p, q)
		printTreeDfs(lca)
		fmt.Println()
	}
}
