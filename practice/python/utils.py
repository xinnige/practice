class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def buildlist(arr):
    if len(arr) == 0:
        return None, []
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0], nodelist


def buildInterList(arr1, arr2, arr3):
    head1, nodelist1 = buildlist(arr1)
    head2, nodelist2 = buildlist(arr2)
    head3, nodelist3 = buildlist(arr3)
    nodelist1[-1].next = head3
    nodelist2[-1].next = head3
    return head1, head2
        

def printList(head):
    p = head
    while p is not None:
        print p.val, "->", 
        p = p.next
    print "None"

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
