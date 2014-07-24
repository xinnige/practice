class Solution:
        
    # @return an integer
    def numTrees(self, n):
        results = [1,1,2]
        for previous in range(3,n+1):
             current = 0
             for i in range(1,previous+1):             
                 current += results[i-1]*results[previous-i]
             results.append(current)
        return results[n]
  
    # @return an integer
    def numTrees_recusive(self, n):
        if n == 0:
            return 1
        if n ==  1:
            return 1
        if n == 2:
            return 2
        counter = 0
        for i in range(1,n+1):
            counter += self.numTrees(n-i)*self.numTrees(i-1)
        return counter



if __name__ == "__main__":
    sol = Solution()
    print sol.numTrees(1)
    print sol.numTrees(2)
    print sol.numTrees(3)
    print sol.numTrees(4)
    print sol.numTrees(5)
