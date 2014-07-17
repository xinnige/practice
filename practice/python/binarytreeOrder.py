# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        pass

    def constructtree(self, head):
        root = TreeNode(head.val)
        while (head.next is not None):
            head = head.next
            self.insertNode(root,head.val)
        self.preordertree(root)
 
    def insertNode(self, node, val):
        if node is not None:
            if val < node.val:
                if node.left is not None:
                    self.insertNode(node.left,val)
                else:
                    node.left = TreeNode(val)
            elif val >= node.val:
                if node.right is not None:
                    self.insertNode(node.right,val)
                else:
                    node.right = TreeNode(val)
            
    def preordertree(self,root):
        if root.left is not None:
            self.preordertree(root.left)
        print root.val
        if root.right is not None:
            self.preordertree(root.right)
 
def buildlist(arr):
    if len(arr) == 0:
        return None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0]
   
if __name__ == "__main__":
     sol = Solution()
     head = buildlist([3,4,7,9,8,1,2,0,6,5])
     sol.constructtree(head)           
     
  

        
