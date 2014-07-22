# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def pathSum(self, root, number):
        patharray = self._getPath(root)
        print patharray
        resultarray = []
        if len(patharray) == 0:
            return resultarray
        sumarray = map(sum,patharray)
        for i in range(len(sumarray)):
            if sumarray[i] == number:
                resultarray.append(patharray[i])
        return resultarray

    # @param node, a tree node
    # @return an list of lists representing all paths from leaf to node as root.
    def _getPath(self,node):
        patharray = []
        if node is None:
            return patharray        
        if node.left is None and node.right is None:
            return [[node.val]]
        if node.left is not None:
            patharray.extend(self._getPath(node.left))
        if node.right is not None:
            patharray.extend(self._getPath(node.right))
        for arr in patharray:
            arr.insert(0,node.val)
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
    #tree = buildtree([1,2,3,'#',4,5,6,'#','#',7])
    tree = buildtree([5,4,8,11,'#',13,4,7,2,'#','#','#','#',5,1])
    #sol._getPath(tree)
    print sol.pathSum(tree,22)
