# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
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

    def preorder(self,root):
        print root.val
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)    

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

if __name__ == '__main__':
    sol = Solution()
    tree = buildtree(['1','2','3','#','4','5','6','#','#','7'])
    #sol.preorder(tree)
    print sol.maxDepth(tree)
