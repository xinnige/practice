# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        current = dummyHead
        first = dummyHead
        counter = 0
        while current.next is not None and counter < n:
            counter += 1
            current = current.next
        while current.next is not None:
            current = current.next
            dummyHead = dummyHead.next
        if dummyHead.next is  None:
            return None
        dummyHead.next = dummyHead.next.next
        
        return first.next
        
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
    #head = buildlist([1,2,3,4,5,6,7,8])
    head = buildlist([1,2])
    #head = buildlist([1])
    #head = buildlist([])
    sol = Solution()
    n = 2
    head = sol.removeNthFromEnd(head,n)
    while head is not None:
        print head.val, "->",
        head = head.next

