# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        previous = ListNode(-65535)
        previous.next = head
        first = previous
        last = previous
        current = previous.next
        front = current.next 
        while front is not None:
            if last.val != current.val and current.val != front.val:
                previous.next = current
                previous = previous.next        
            last = last.next
            current = current.next
            front = front.next
        if last.val == current.val:
            previous.next = None 
        else:
            previous.next = current
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
    head = buildlist([1,1,2,2])
    head = buildlist([1,2,2])
    head = buildlist([1,1,2,3,3,4,4,5])
    head = buildlist([1])
    head = buildlist([])
    sol = Solution()
    head = sol.deleteDuplicates(head)
    while head is not None:
        print head.val, '->',
        head = head.next
    

