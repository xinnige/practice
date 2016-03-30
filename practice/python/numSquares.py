class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxSquare = int(n ** 0.5)

        dynamic_map=range(n+1)
        print dynamic_map
        for i in range(1, maxSquare):
            for j in range(1, n+1):
                if j >= (i+1)**2:
                    dynamic_map[j] = min(dynamic_map[j], dynamic_map[j-(i+1)**2]+1)
            print dynamic_map
        return dynamic_map[-1]
   
       
sol = Solution()
print sol.numSquares(17)

 
