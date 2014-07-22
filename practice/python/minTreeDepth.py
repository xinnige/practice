# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param node, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        leftdepth,rightdepth = 0,0
        if root.left is not None:
            leftdepth = self.minDepth(root.left)
        if root.right is not None:
            rightdepth = self.minDepth(root.right)
        if leftdepth != 0 and rightdepth == 0:
            return leftdepth+1
        if leftdepth == 0 and rightdepth != 0:
            return rightdepth+1
        return min(leftdepth,rightdepth)+1

    def preorder(self,node):
        print node.val
        if node.left is not None:
            self.preorder(node.left)
        if node.right is not None:
            self.preorder(node.right)    

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
    #tree = buildtree(['1','2','3','8','4','5','6','#','#','7'])
    tree = buildtree(['1'])
    #tree = buildtree(['1','2','#','3'])
    #sol.preorder(tree)
    print sol.minDepth(tree)
