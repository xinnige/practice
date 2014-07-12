# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        step1 = head 
        step2 = head
        cyclic = False
        while(step1 is not None and step2 is not None and step2.next is not None):
            step1 = step1.next
            
            step2 = step2.next.next
            if step1 == step2:
                cyclic = True
                break
        return cyclic 
 
def buildlist(arr):
    if len(arr) == 0:
        return None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0], nodelist

def makecycle(nodelist,i,j):
    nodelist[i].next = nodelist[j]

if __name__ == '__main__':
    head, nodelist = buildlist([1])
#    head, nodelist = buildlist([0,1,2,3,4,5,6,7,8,9])
#    makecycle(nodelist,9,5)
    sol = Solution()
    print sol.hasCycle(head)
