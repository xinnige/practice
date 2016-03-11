class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            print n, 
            n &= n-1
            count += 1
        return count


sol = Solution()
print sol.hammingWeight(11)
print sol.hammingWeight(0)
print sol.hammingWeight(1)
print sol.hammingWeight(15)
print sol.hammingWeight(16)
