# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def rotateRight(self, head, n):
        if head is None:
            return head
        dummyHead = head
        current = dummyHead
        first = dummyHead
        counter = 0
        end = None 
        while counter < n:
            counter += 1
            if current.next is None:
                end = current
                current.next = first
            current = current.next
        if end is not None:
            end.next = None
        while current.next is not None:
            current = current.next
            dummyHead = dummyHead.next
        current.next = first
        head = dummyHead.next
        dummyHead.next = None 
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

if __name__ == "__main__":
    head = buildlist([1,2,3,4,5,6,7,8])
    head = buildlist([1,2])
    #head = buildlist([1])
    #head = buildlist([])
    sol = Solution()
    n = 0 
    head = sol.rotateRight(head,n)
    counter = 0
    while head is not None and counter < 15:
        print head.val, "->",
        head = head.next
        counter += 1

