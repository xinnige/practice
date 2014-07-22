# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def hasPathSum(self, root, number):
        patharray = self._getPathSum(root)
        if len(patharray) == 0:
            return False
        if number in patharray:
            return True
        return False

    # @param node, a tree node
    # @return an list of lists representing all paths from leaf to node as root.
    def _getPathSum(self,node):
        patharray = []
        if node is None:
            return patharray        
        if node.left is None and node.right is None:
            return [node.val]
        if node.left is not None:
            for i in self._getPathSum(node.left):
                patharray.append(i+node.val)
        if node.right is not None:
            for i in self._getPathSum(node.right):
                patharray.append(i+node.val)
        return patharray
# 
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
    #tree = buildtree([])
    tree = buildtree([5,4,8,11,'#',13,4,7,2,'#','#','#','#','#',1])
    #tree = buildtree([1,2,3,'#',4,5,6,'#','#',7])
    print sol.hasPathSum(tree,22)
