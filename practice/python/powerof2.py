class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        print n,
        count = self.hammingWeight(n)
        if count == 1:
            return True
        return False

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n-1
            count += 1
            if count > 1:
                break
        return count

sol = Solution()
print sol.isPowerOfTwo(0)
print sol.isPowerOfTwo(1)
print sol.isPowerOfTwo(2)
print sol.isPowerOfTwo(3)
print sol.isPowerOfTwo(4)
print sol.isPowerOfTwo(8)
print sol.isPowerOfTwo(9)
print sol.isPowerOfTwo(16)
print sol.isPowerOfTwo(100)
print sol.isPowerOfTwo(128)
