# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node is None:
            return
        if node.next is None:
            node = None
            return
        node.val = node.next.val
        node.next = node.next.next
        return


def printlist(headnode):
    current = headnode
    while current:
         print current.val, "->", 
         current = current.next
    print "None"


def buildlist(arr):
    if len(arr) == 0:
        return None
    nodelist = []
    for number in arr:
        nodelist.append(ListNode(number))

    for i in range(len(nodelist)-1):
        nodelist[i].next=nodelist[i+1]
    return nodelist[0], nodelist


if __name__ == '__main__':
    head, nodelist = buildlist([0,1,2,3,4,5,6,7,8,9])
    printlist(head)
    sol = Solution()
    sol.deleteNode(nodelist[4])
    printlist(head)

