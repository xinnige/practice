# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def preorderTraversal(self,root):
        return self.iterator([root])


    def iterator(self,iterstack):
        values = []
        while len(iterstack) != 0:
            node = iterstack.pop()
            if node is not None:
                values.append(node.val)
                if node.right is not None:
                    iterstack.append(node.right)
                if node.left is not None:
                    iterstack.append(node.left)
        return values


    def _preorderTraversal(self, root):
        self.recursive(root)

    def recursive(self,node):
        if node.val == '#':
            return
        print node.val
        if node.left != None:
            self.recursive(node.left)
        if node.right != None:
            self.recursive(node.right) 
        
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
#    for node in nodearr:
#        print node.val
#        if node.left:
#            print node.left.val
#        if node.right:
#            print node.right.val

    if len(nodearr) > 0:
        return nodearr[0]
    return None

 

if __name__ == '__main__':
    sol = Solution()
    #root = buildtree([1,'#',2,'#','#','#',3])
    #root = buildtree([1,2,5,3,4,6,7])
    #root = None
    #root = buildtree([1])
    root = buildtree([1,2,4,3,'#',5,6,'#','#','#','#','#',7])
    print sol.preorderTraversal(root)











