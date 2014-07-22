# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
   
class Solution:
    # @param root, a tree node
    # @return nothing
    def fulfilltree(self, root):
        maxdepth = self.maxDepth(root)
        self._fullfilltree(root,0,maxdepth)

    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        leftdepth,rightdepth = 0,0
        if root.left is not None:
            leftdepth = self.maxDepth(root.left)
        if root.right is not None:
            rightdepth = self.maxDepth(root.right)
        return max(leftdepth,rightdepth)+1

    def _fullfilltree(self, node, level, maxdepth):
        if node is None:
            return
        if node.left is None and node.right is None and level == maxdepth-1:
            return
        if node.left is None:
            node.left = TreeNode("#")
        if node.right is None:
            node.right = TreeNode("#")
        self._fullfilltree(node.left,level+1,maxdepth)
        self._fullfilltree(node.right,level+1,maxdepth)

def preorder(node):
    if node is None:
        return
    print node.val,
    preorder(node.left)
    preorder(node.right) 

def buildtree(arr):
    nodearr = []
    for number in arr:
        nodearr.append(TreeNode(number))
    for i in range(1,len(nodearr)):
        node = nodearr[i]
        if node.val == "#":
            continue
        if i%2 == 1:
            nodearr[i/2].left = node
        else:
            nodearr[(i/2)-1].right = node

    if len(nodearr) > 0:
        return nodearr[0]
    return None

if __name__ == "__main__":
    sol = Solution()
    tree = buildtree([])
    #tree = buildtree([1])
    #tree = buildtree([1,2,3,'#',4,5,6,'#','#',7])
    #tree = buildtree([5,4,8,11,'#',13,4,7,2,'#','#','#','#','#',1])
    #tree = buildtree([1,2,2,'#',3,'#',3])
    #tree = buildtree([1,2,2,3,4,4,3])
    #tree = buildtree([1,2,2,5,3,3,5,'#','#','#',4,'#','#',4])
    #tree = buildtree([3,9,20,'#','#',15,7])
    #tree = buildtree([1,2,3,3,'#',2,'#'])
    tree = buildtree([5,4,1,'#',1,'#',4,'#','#',2,'#','#','#',2,'#'])
    sol.fulfilltree(tree)
    preorder(tree)
