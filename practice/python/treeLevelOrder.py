# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def levelOrder(self, root):
        leveldict = {}
        self._arrange(root,0, leveldict)
        index = 0
        result = []
        while leveldict.has_key(index):
            result.append(leveldict[index])
            index += 1
        return result
    # @param node, a tree node
    # @return an list of lists representing all paths from leaf to node as root.
    def _arrange(self, node, current_level, leveldict):
        if node is None:
            return       
        if not leveldict.has_key(current_level):
            leveldict[current_level] = []
        leveldict[current_level].append(node.val)
        if node.left is not None:
            self._arrange(node.left, current_level+1, leveldict)
        if node.right is not None:
            self._arrange(node.right,current_level+1, leveldict)
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
    tree = buildtree([])
    tree = buildtree([1])
    #tree = buildtree([1,2,3,'#',4,5,6,'#','#',7])
    #tree = buildtree([5,4,8,11,'#',13,4,7,2,'#','#','#','#','#',1])
    #tree = buildtree([3,9,20,'#','#',15,7])
    #sol._getPath(tree)
    print sol.levelOrder(tree)
