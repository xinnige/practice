class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            title = chr(remainder+65) + title
        return title


sol = Solution()
for i in range(1, 100):
    print sol.convertToTitle(i),

print
print sol.convertToTitle(51)
print sol.convertToTitle(52)
print sol.convertToTitle(53)
print sol.convertToTitle(676)
print sol.convertToTitle(702)


