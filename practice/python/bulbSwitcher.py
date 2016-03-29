class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)

sol = Solution()
for i in range(50):
    print i, sol.bulbSwitch(i)
