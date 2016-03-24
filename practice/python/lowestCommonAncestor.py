from utils import buildtree


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p is None or q is None or root is None:
            return
        if root.val == p.val or root.val == q.val:
            return root
        if (p.val < root.val and q.val > root.val) or \
           (p.val > root.val and q.val < root.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # other condition is  p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q) 



sol = Solution()
#tree = buildtree([])
#tree = buildtree([1])
tree = buildtree([6,2,8,0,4,7,9,None,1,3,5])
tree = buildtree([2,1,3])
p = TreeNode(3)
q = TreeNode(1)         
print sol.lowestCommonAncestor(tree, p, q).val
