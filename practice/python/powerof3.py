class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n >= 3 and n%3 == 0:
            n = n/3
        return n == 1
        
if __name__ == "__main__":
        sol = Solution()
        sol.isPowerOfThree(1)
        sol.isPowerOfThree(3)
        sol.isPowerOfThree(8)
        sol.isPowerOfThree(9)
        sol.isPowerOfThree(45)
        sol.isPowerOfThree(243)
        sol.isPowerOfThree(729)
        sol.isPowerOfThree(3**8+1)
        sol.isPowerOfThree(3**8+3)
        sol.isPowerOfThree(3**8)
