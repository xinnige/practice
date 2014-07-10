# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None:
            return head
        nodelist = []
        node = head
        while(node):
            nodelist.append(node)
            node = node.next
        
        for i in range(len(nodelist)/2):
            j = len(nodelist)-1-i
            nodelist[i].next = nodelist[j]
            nodelist[j].next = nodelist[i+1]
        nodelist[len(nodelist)/2].next = None
  
        return head

def buildlist(arr):
    if len(arr) == 0:
        return None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0]


if __name__=='__main__':
    #head = buildlist([1,2,3,4,5,6,7,8,9])
    #head = buildlist([1,2,3,4,5,6,7,8])
    #head = buildlist([])
    head = buildlist([1])
    sol = Solution()
    head = sol.reorderList(head)
    while head is not None:
        print head.val
        head = head.next
