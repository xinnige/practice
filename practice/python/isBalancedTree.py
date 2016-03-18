from utils import buildtree, preOrder, postOrder

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.result = True

    def cal_depth(self, root):
        leftdepth = 0
        rightdepth = 0
        if root is None:
            return
        if root.left:
            if hasattr(root.left, "depth"):
                leftdepth = root.left.depth
            else:
                leftdepth = self.cal_depth(root.left)
        if root.right:
            if hasattr(root.right, "depth"):
                rightdepth = root.right.depth
            else:
                rightdepth = self.cal_depth(root.right)
        if leftdepth is None or rightdepth is None:
            return
        if leftdepth > rightdepth + 1  or leftdepth < rightdepth - 1:
            self.result = False
            return
        depth = max(leftdepth, rightdepth)+1
        setattr(root, "depth", depth)
        return depth
 
    def _isBalanced(self, node):
        isBalanced = True
        if node is None:
            return True
        if node.left and node.right:
            if node.left.depth > node.right.depth + 1 or node.left.depth < node.right.depth - 1:
                return False
            else :
                if not self._isBalanced(node.left):
                    return False
                if not self._isBalanced(node.right):
                    return False
        else:
            if node.depth > 2:
                return False
        return True
        
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.cal_depth(root)
        return self.result


sol = Solution()
tree = buildtree([6,2,8,0,4,7,9,None,1,3,5])
print sol.isBalanced(tree)
preOrder(tree)
 
tree = buildtree([1])
print sol.isBalanced(tree)
preOrder(tree)

tree = buildtree([])
print sol.isBalanced(tree)
preOrder(tree)

tree = buildtree([1,2,3,4,5,None,None,8,9,None,None,None,None,None,None,10])
print sol.isBalanced(tree)
preOrder(tree)
