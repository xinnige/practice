# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p2 = head
        pp1 = head
        if p2 == None:
            return head
        p1 = head.next
        if p1 == None:
            return head
        count = 2
        while p2 is not None:
            print head.val
            pp2, p2 = self.walkNstep(p2, count)
            if p2 == None:
                return head
            pp2.next = p2.next
            p2.next = p1
            pp1.next = p2
            count += 1
            tp, pp1 = self.walkNstep(pp1, 1)
        return head
        
    def walkNstep(self, pnode, n):
        while n > 1 and pnode.next is not None:
            pnode = pnode.next
            n = n - 1            
        return pnode, pnode.next

def buildlist(arr):
    if arr is None or len(arr) == 0:
        return None, None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0], nodelist

def printLink(head):
    phead = head
    while phead is not None:
       print phead.val, '->',
       phead = phead.next 
    print "None"

if __name__ == "__main__":
    head, nodelist = buildlist([1,2,3,4,5,6,7,8,9])
    #head, nodelist = buildlist([1,2,3,4,5,6,7,8])
    #head, nodelist = buildlist([1,2,3])
    sol = Solution()
    head = sol.oddEvenList(head)
    printLink(head)

    
    
    
