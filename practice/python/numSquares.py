class Solution(object):
    def __init__(self):
        self.dynamic_map = [0]    

    def numSquares(self, n):
        if len(self.dynamic_map) <= n:
            maxSquare = int(n ** 0.5)
            items = [(i+1)**2 for i in range(maxSquare)]
            for i in range(len(self.dynamic_map), n+1):
                self.dynamic_map.append(min(1+self.dynamic_map[i-square] for square in items if square <= i))

        return self.dynamic_map[n]  

sol = Solution()
print sol.numSquares(17)
print sol.dynamic_map

 
