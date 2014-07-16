# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return None
        nodelist = [head]
        while head.next is not None :
            head = head.next
            if head.val <= nodelist[0].val:
                nodelist.insert(0,head)
                continue
            elif head.val >= nodelist[-1].val:
                nodelist.append(head)
                continue

            pointer = -1
            for i in range(len(nodelist)-1):
                if head.val >= nodelist[i].val and head.val <= nodelist[i+1].val:
                    pointer = i
                    break
            if pointer != -1:
                nodelist.insert(pointer+1,head)

 
        for i in range(len(nodelist)-1):
            nodelist[i].next = nodelist[i+1]
        nodelist[-1].next = None
        return nodelist[0]
        


def buildlist(arr):
    if len(arr) == 0:
        return None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0]
  

if __name__ == '__main__':
    sol = Solution()
    head = buildlist([0,4,6,3,1,5,7,1,3,5])
    #head = buildlist([0])
    head = None
    head = sol.insertionSortList(head)
    while head is not None:
         print head.val,
         head = head.next
