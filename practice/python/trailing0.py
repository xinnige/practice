class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        return self.trailingZeroes(n/5) + n/5 

sol = Solution()
print sol.trailingZeroes(1)
print sol.trailingZeroes(20)
print sol.trailingZeroes(100)        

