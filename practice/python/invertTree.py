# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.iterator([(root,0)])
        return root
        

    def _invertNode(self, root):
        tmp = root.left
        root.left = root.right
        root.right = tmp

    def iterator(self,iterstack):
        while len(iterstack) != 0:
            node,read = iterstack.pop()
            if node is not None:
                if read == 1:
                    self._invertNode(node)
                else:    
                    iterstack.append((node,1))
                    if node.right is not None:
                        iterstack.append((node.right,0))
                    if node.left is not None:
                        iterstack.append((node.left,0))
        

def buildtree(arr):
    nodearr = []
    for number in arr:
        nodearr.append(TreeNode(number))
    for i in range(1,len(nodearr)):
        node = nodearr[i]
        if i%2 == 1:
            nodearr[i/2].left = node
        else:
            nodearr[(i/2)-1].right = node

    if len(nodearr) > 0:
        return nodearr[0]
    return None

def preorder(node):
    print node.val,
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

if __name__ == '__main__':
    sol = Solution()
    #root = buildtree([1,2,4,3,'#',5,6,'#','#','#','#','#',7])
    root = buildtree([1])
    print preorder(root)
    sol.invertTree(root)
    print preorder(root)

