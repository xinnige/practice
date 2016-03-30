class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxSquare = int(n ** 0.5)
        items = []
        for i in range (1, maxSquare+1):
            items.append(i**2)

        dynamic_map = []
        for i in range (maxSquare):
            if i == 0:
                dynamic_map.append(range(n+1))
            else:
                dynamic_map.append([0, 1]+[None]*(n-1))

        for i in range(1, maxSquare):
            for j in range(2, n+1):
                if j >= items[i]:
                    dynamic_map[i][j] = min(dynamic_map[i-1][j], dynamic_map[i][j-items[i]]+1)
                else:
                    dynamic_map[i][j] = dynamic_map[i-1][j]

        return dynamic_map[maxSquare-1][n]
   

def print2DArray(array, m, n):
    for i in range(m):
        for j in range(n):
            print array[i][j], 
        print
       
sol = Solution()
print sol.numSquares(17)

 
