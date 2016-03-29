class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0]*n
        for i in range(1, n+1):
            for j in range(i-1, n, i):
                arr[j] = (arr[j] + 1) % 2
        return sum(arr)
        

sol = Solution()
for i in range(50):
    print i, sol.bulbSwitch(i)
