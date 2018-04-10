import utils

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverse(self, startpoint):
        current = startpoint
        previous = utils.ListNode(None)
        previous.next = current
        while current.next is not None:
            cnext = current.next.next        
            previous = current
            current = tmp
        startpoint = None
        return current 

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        cursor = head
        tail = None
        midpint = None
        count = 1 
        while tail.next is not None:
            tail = tail.next
            count += 1
        midpoint = (count+1)/2
        count = 0 
        midpoint = head
        print count, tail.val
        


sol = Solution()
#head, nodes = utils.buildlist([])
#head, nodes = utils.buildlist([1])
#head, nodes = utils.buildlist([1,2,3,2,1])
head, nodes = utils.buildlist([1,2,3,4,5])
sol.reverse(head)
utils.printList(head)
#sol.isPalindrome(head)
