class Solution(object):
    def helper(self, m , n):
        if m == 1 and n == 1:
            return 0 
        if m == 1:
            return 1
        if m == 2:
            return n
        if m == n:
            return 2 * self.helper(m-1, n)
        return self.helper(m-1 ,n) + self.helper(m, n-1)

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= n:
            return self.helper(m, n)
        else:
            return self.helper(n, m)
          

sol = Solution()
print sol.uniquePaths(1,2)
print sol.uniquePaths(2,2)
print sol.uniquePaths(2,3)
print sol.uniquePaths(3,3)
print sol.uniquePaths(3,4)
print sol.uniquePaths(4,4)
print sol.uniquePaths(4,5)
print sol.uniquePaths(12,23)
