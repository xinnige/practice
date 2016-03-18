class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildtree(arr):
    nodearr = []
    for number in arr:
        nodearr.append(TreeNode(number))
    for i in range(1,len(nodearr)):
        node = nodearr[i]
        if node.val is None:
            continue
        if node.val == "#":
            continue 
        if i%2 == 1:
            nodearr[i/2].left = node
        else:
            nodearr[(i/2)-1].right = node
    if len(nodearr) > 0:
        return nodearr[0]
    return None

def preOrder(root):
    if root is not None:
        print (root.val, ), 
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root is not None:
        postOrder(root.left)
        postOrder(root.right)
        print root.val, 
