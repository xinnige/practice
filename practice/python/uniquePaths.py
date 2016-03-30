class Solution(object):
    def __init__(self):
        self.pathmap = None 

    def helper(self, m, n):
        self.pathmap = list() 
        self.pathmap.append([1]*n)
        for row in range(1, m):
            self.pathmap.append([1]+[0]*(n-1))

        for r in range(1, m):
            for c in range(1, n):
                self.pathmap[r][c] = self.pathmap[r-1][c] + self.pathmap[r][c-1]

        # print2DArray(self.pathmap, m, n) 


    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.helper(m, n)
        return self.pathmap[m-1][n-1]
          

def print2DArray(array, m, n):
    for i in range(m):
        for j in range(n):
            print array[i][j], 
        print


sol = Solution()
print sol.uniquePaths(1,2)
print sol.uniquePaths(2,2)
print sol.uniquePaths(2,3)
print sol.uniquePaths(3,3)
print sol.uniquePaths(3,4)
print sol.uniquePaths(4,4)
print sol.uniquePaths(4,5)
print sol.uniquePaths(5,5)
print sol.uniquePaths(12,23)
