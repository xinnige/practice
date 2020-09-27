package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestLowerCommonAncestor(t *testing.T) {
	tests := []struct {
		nodes  []int
		p      int
		q      int
		expect int
	}{
		{[]int{3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4}, 5, 1, 3},
		{[]int{3, 5, 1, 6, 2, 0, 8, -1, -1, 7, 4}, 5, 4, 5},
	}
	for _, tc := range tests {
		root := formatTree(tc.nodes)
		p := searchTreeNode(root, tc.p)
		q := searchTreeNode(root, tc.q)
		lca := lowestCommonAncestor(root, p, q)
		assert.Equal(t, tc.expect, lca.Val)
	}
}
