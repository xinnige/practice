import utils
               
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        previous = ListNode(None)
        previous.next = head
        source = previous
        current = head
        while current is not None:
            if current.val == val:
                current = current.next
                continue
            previous.next = current
            previous = current
            current = current.next
        previous.next = current
        return source.next 
        
sol = Solution()
head, arr = utils.buildlist([1,2,3,4,5,6,7,1,2,3,4,5,6,7,3,3,3,3,4,4,5,6,4,3])
#head, arr = utils.buildlist([3,3,3,3,3])
#head, arr = utils.buildlist([1,2,3])
#head, arr = utils.buildlist([3])
utils.printList(head)
source = sol.removeElements(head, 3)
utils.printList(source)

