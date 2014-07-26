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
        current = head
        previous = ListNode(-65535)
        previous.next = head
        first = previous
        #print current.val, previous.val
        while current is not None:
            if current.val == previous.val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
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
    head = buildlist([1,1,2])
    #head = buildlist([1,2,2])
    head = buildlist([1,1,2,3,3])
    head = buildlist([1])
    head = buildlist([])
    sol = Solution()
    head = sol.deleteDuplicates(head)
    while head is not None:
        print head.val, '->',
        head = head.next
    

