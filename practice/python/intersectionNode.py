import utils

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def countSize(self, head):
        counter = 0
        p = head
        while p is not None:
            p = p.next
            counter += 1
        return counter

    def walk(self, longHead, shortHead, delta):
        for i in range(delta):
            longHead = longHead.next 
        if longHead == shortHead:
            return longHead
        while longHead.next != shortHead.next:
            longHead = longHead.next
            shortHead = shortHead.next
        return longHead.next

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        if headA == headB:
            return headA
        sizeA = self.countSize(headA)
        sizeB = self.countSize(headB) 
        if sizeA > sizeB:
            return self.walk(headA, headB, sizeA-sizeB)
        return self.walk(headB, headA, sizeB-sizeA) 

head1, head2 = utils.buildInterList([1,2,3,4],[5,6,7],[8,9,10,11,12])
head1, head2 = utils.buildInterList([1,2,3,4],[5,6,7,8,9,10,11],[18,19,110,111,112])
head1, head2 = utils.buildInterList([1,2],[5],[8,9,10])
head2.next = head1.next
utils.printList(head1)
utils.printList(head2)
sol = Solution()
inode = sol.getIntersectionNode(head1, head2)
if inode:
    print inode.val
else:
    print inode


