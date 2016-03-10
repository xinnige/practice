# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        next = head.next
        head.next = None
        while next is not None:
            nnext = next.next
            next.next = head
            head = next
            next = nnext
        return head
        
        
def printlist(headnode):
    current = headnode
    while current:
         print current.val, "->", 
         current = current.next
    print "None"


def buildlist(arr):
    if len(arr) == 0:
        return None, None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0], nodelist

if __name__ == '__main__':
    head, nodelist = buildlist([])
    #head, nodelist = buildlist([0,1,2,3,4,5,6,7,8,9])
    printlist(head)
    sol = Solution()
    head = sol.reverseList(head)
    printlist(head)

