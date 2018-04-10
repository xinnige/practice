class Solution(object):
    def numSquares(self, n):
        sums = {0}
        while n not in sums:
            sums = {s + i*i
                    for s in sums
                    for i in range(1, int((n - s)**0.5 + 1))}
            print sums
        return min(sums)

sol = Solution()
print sol.numSquares(17)

 
