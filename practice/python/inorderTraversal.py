# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    
   
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        return self.iterator([(root,False)])

    def _printstack(self, inorderstack):
        print [(node.val,isread) for node,isread in inorderstack]

    def iterator(self,inorderstack):
        result = []
        while len(inorderstack) != 0:
            #self._printstack(inorderstack)
            node,leftread = inorderstack.pop()
            if node is not None:
                if not leftread:
                    inorderstack.append((node,True))
                    if node.left is not None:
                        inorderstack.append((node.left,False))
                else:
                    result.append(node.val)
                    if node.right is not None:
                        inorderstack.append((node.right,False))
        return result

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

if __name__ == "__main__":
    sol = Solution()
    #root = buildtree([1,'#',2,3])
    #root = buildtree([1,'a',2,'b','c',3])
    root = buildtree([1])
    #root = buildtree([1,'#',2,'#','#','#',3])
    print sol.inorderTraversal(root)
