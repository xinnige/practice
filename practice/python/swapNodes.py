import utils

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        nextNode = head.next
        if nextNode is None:
            return head
        
        source = utils.ListNode(None)
        source.next = head
        previous = source
        while head is not None and nextNode is not None:
            previous.next = nextNode
            afterNext = nextNode.next
            head.next = afterNext
            nextNode.next = head
            previous = head
            head = afterNext
            if head is None:
                break
            nextNode = head.next
            if nextNode is None:
                break
            # utils.printList(source.next)
            # if nextNode.next is not None:
            #     print "previous %s, head %s, next %s, afternext %s" % (previous.val, head.val, nextNode.val, nextNode.next.val)
                      
        return source.next

         
sol = Solution()
#head, lista = utils.buildlist([])
#head, lista = utils.buildlist([1])
#head, lista = utils.buildlist([1,2])
#head, lista = utils.buildlist([1,2,3])
#head, lista = utils.buildlist([1,2,3,4])
#head, lista = utils.buildlist([1,2,3,4,5])
# head, lista = utils.buildlist([1,2,3,4,5,6,7,8])
head = sol.swapPairs(head)
utils.printList(head)
