class Solution:
    def combine(self, n, k):
        result = []
        if k <= 0 or n <= 0 or k > n:
            return []
        if k == 1:
            theresult = []
            for i in range(n):
                theresult.append([i+1])
            return theresult
        if n == k:
            return [[i+1 for i in range(n)]]
        result = self.combine(n-1,k)
        result2 = self.combine(n-1,k-1)
        for i in result2:
            i.append(n)
            result.append(i)
        return result



if __name__ == "__main__":
    sol = Solution()
    #print sol.combine(4,1)
    print sol.combine(6,4)
    print sol.combine(6,0)
    print sol.combine(1,1)
    print sol.combine(2,1)
    print sol.combine(0,1)
