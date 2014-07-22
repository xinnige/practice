# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return root
        nodelist = []
        self._preorder(root,nodelist)
        for i in range(len(nodelist)-1):
            nodelist[i].left = None
            nodelist[i].right = nodelist[i+1]
        nodelist[-1].left = None
        nodelist[-1].right = None
        return nodelist[0]
            


    def _preorder(self, node, nodelist):
        nodelist.append(node)
        if node.left is not None:
            self._preorder(node.left,nodelist)
        if node.right is not None:
            self._preorder(node.right,nodelist) 
 
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

def preorder(node):
    if node is None:
        return
    print node.val
    if node.left is not None:
        preorder(node.left)
    if node.right is not None:
        preorder(node.right)

if __name__ == '__main__':
    sol = Solution()
    tree = buildtree([1])
    #tree = buildtree([1,2,3,'#',4,5,6,'#','#',7])
    #tree = buildtree([5,4,8,11,'#',13,4,7,2,'#','#','#','#','#',1])
    #sol._getPath(tree)
    preorder(sol.flatten(tree))
