# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.compareNodes(root.left,root.right)

    def compareNodes(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        leftside = self.compareNodes(node1.left, node2.right)
        rightside = self.compareNodes(node1.right, node2.left)
        return leftside and rightside


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
    tree = buildtree([1,2,2,3,4,4,3])
    #tree = buildtree([1,2,2,5,3,3,5,'#','#','#',4,'#','#',4])
    #tree = buildtree([3,9,20,'#','#',15,7])
    #tree = buildtree([1,2,3,3,'#',2,'#'])
    #tree = buildtree([5,4,1,'#',1,'#',4,'#','#',2,'#','#','#',2,'#'])
    print sol.isSymmetric(tree)
