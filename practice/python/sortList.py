# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.next = None
        self.val = x

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        step = 1
        size = self.getListSize(head)
        while head is not None and step < size:
            print head.val , step
            head = self.orderOnce(head,step)
            self.printList(head)
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

    def printList(self,head):
        print "list:"
        current = head
        while current is not None:
             print current.val, '-',
             current = current.next
        print


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
    #head = buildlist([9,4,3,6,2,6,3,1,2,0,5,4])
    head = buildlist([9,1,4,2,7,8,6,0,5,3])
    sol = Solution()
    head = sol.sortList(head)
    print
    while head is not None:
        print head.val, '->',
        head = head.next
