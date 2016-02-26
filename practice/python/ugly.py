#!/bin/python

# Ugly number: Prime Factor contains only 2, 3, 5
# 1 is treated as Ugly number

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        print num,
        if num == 0:
            return False
        if num == 1:
            return True
        while num != 1:
            if num % 2 == 0:
               num = num/2
               continue
            if num % 3 == 0:
               num = num/3
               continue
            if num % 5 == 0:
               num = num/5
               continue
            if num != 1:
               return False
        return True

sol = Solution()
print sol.isUgly(2)
print sol.isUgly(3)
print sol.isUgly(5)
print sol.isUgly(0)
print sol.isUgly(1)
print sol.isUgly(6)
print sol.isUgly(2)
print sol.isUgly(15)
print sol.isUgly(20)
print sol.isUgly(12)
print sol.isUgly(35)

            
