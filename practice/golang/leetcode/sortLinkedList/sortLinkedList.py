# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        step = 1
        size = self.getListSize(head)
        while head is not None and step < size:
            head = self.orderOnce(head,step)
            step *= 2
        return head

    def orderOnce(self, head,step):
        previoustail = None
        top = None
        while head is not None:
            # reorder every step nodes and join them
            node1, node2, nexthead = self.getTwoList(head,step)
            head,tail = self.switch(node1,node2)        
            if previoustail is not None:
                previoustail.next = head
            previoustail = tail
            if top is None:
                top = head
            tail.next = nexthead       
            head = tail.next
        return top

    def getListSize(self,head):
        counter = 0
        while head is not None:
            head = head.next
            counter += 1
        return counter

 
    def getTwoList(self, head, step):
        # reorder every step nodes and join them
        node1 = head
        counter = 0
        while head is not None and counter < step-1:
            head = head.next
            counter += 1
        if head is None:
            return node1, None, None
        node2 = head.next
        head.next = None
        head = node2
        counter = 0
        while head is not None and counter < step-1:
            head = head.next
            counter += 1
        nexthead = None
        if head is not None:
            nexthead = head.next                  
            head.next = None
        return node1, node2, nexthead
 

    def switch(self, node1, node2):
        previous = None
        head = None
        if node2 is None:
            head = node1
            previous = node1
            while previous.next is not None:
                previous = previous.next
            return head, previous


        if node1.val < node2.val:
            previous = node1
            node1 = node1.next
        else:
            previous = node2
            node2 = node2.next
        head = previous
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                previous.next = node1
                node1 = node1.next
            else:
                previous.next = node2
                node2 = node2.next
            previous = previous.next
        if node2 is not None:
            previous.next = node2
        if node1 is not None:
            previous.next = node1
        while previous.next is not None:
            previous = previous.next
        #print "after switch:", head.val, previous.val
        return head,previous
