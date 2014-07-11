# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers

    def postorderTraversal(self,root):
        return self.iterator([(root,0)])


    def iterator(self,iterstack):
        values = []
        while len(iterstack) != 0:
            node,read = iterstack.pop()
            if node is not None:
                if read == 1:
                    values.append(node.val)
                else:    
                    iterstack.append((node,1))
                    if node.right is not None:
                        iterstack.append((node.right,0))
                    if node.left is not None:
                        iterstack.append((node.left,0))
        return values


    def _postorderTraversal(self, root):
        self.recursive(root)

    def recursive(self,node):
        if node is None or node.val == '#':
            return
        if node.left != None:
            self.recursive(node.left)
        if node.right != None:
            self.recursive(node.right) 
        print node.val
        
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
    sol._postorderTraversal(root)
    print sol.postorderTraversal(root)











