class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        results = []
        for i in range(0,numRows):
            itharray = [None]*(i+1)
            for j in range(0,i+1):
                if j == 0 or j == i:
                    itharray[j] = 1
                else:
                    itharray[j]=results[i-1][j-1]+results[i-1][j]
            results.append(itharray)
        return results


if __name__ == "__main__":
    sol = Solution()
    print sol.generate(1)
    print sol.generate(2)
    print sol.generate(3)
    print sol.generate(4)
    print sol.generate(5)
    print sol.generate(6)
