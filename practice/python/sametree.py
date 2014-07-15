# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        qstack = [q]
        pstack = [p]
        return self.iterator(pstack,qstack)


    def iterator(self, pstack, qstack): 
        while(len(pstack) != 0 and len(qstack) != 0):
            pnode = pstack.pop()
            qnode = qstack.pop()
            isTrue = self.isSameNode(pnode,qnode)
            if not isTrue:
                return False
            if pnode is not None and qnode is not None:
                pstack.append(pnode.right)
                pstack.append(pnode.left)
                qstack.append(qnode.right)
                qstack.append(qnode.left)
        if len(pstack) + len(qstack) != 0:
            return False
        return isTrue

    def isSameNode(self, pnode, qnode):
        if pnode is None and qnode is None:
            return True
        if pnode is not None and qnode is None:
            return False
        if pnode is None and qnode is not None:
            return False
        if pnode.val == qnode.val:
            return True
        return False
        
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
 

if __name__ == '__main__':
    sol = Solution()
    #q = buildtree([1,'#',2,'#','#','#',3])
    #p = buildtree([1,'#',2,'#','#',3])

    q = buildtree([1,'#',3])
    p = buildtree([1,'#',2])
    print sol.isSameTree(q,p)
