class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return [1]
        results = [1]*(numRows+1)
        for i in range(0,numRows+1):
            for j in range(i,0,-1):
                if j == 0 or j == i:
                    results[j] = 1
                else:
                    results[j]=results[j-1]+results[j]
        return results


if __name__ == "__main__":
    sol = Solution()
    print sol.generate(1)
    print sol.generate(2)
    print sol.generate(3)
    print sol.generate(4)
    print sol.generate(5)
    print sol.generate(6)
