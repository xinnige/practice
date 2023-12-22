class Solution(object):
    def combination(self, n, m):
        """
		:type n, m: int (n > m)
        :rtype: int C(n, m)
		"""
        if m == 0 or m == n:
            return 1
        if m > (n - m):
            m = n - m
        result = 1
        for i in range(n-m+1, n+1):
            result *= i
        permutate_m = 1
        for i in range(1, m+1):
            permutate_m *= i
        # print "n %d, m %d, result %d / %d" %(n, m, result, permutate_m)
        return result/permutate_m

    def climbStairs_slow(self, n):
        """
        :type n: int
        :rtype: int
        """
        max2Step = n/2
        total = 0
        for i in range(max2Step + 1):
            total += self.combination(n-i, i)
        return total

    def climbStairs_fib(self, n):
        """
		f(n) = f(n-1) + f(n-2) the Fibonacci
        Recusive is just too slow
		"""
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_notAccurate(self, n):
        import math
        import decimal
        gmean = decimal.Decimal(math.sqrt(5))
        phi = (1+gmean)/2
        aphi = (1-gmean)/2
        return int( (phi**(n+1) - aphi**(n+1)) / gmean)

sol = Solution()
print (sol.climbStairs(1))
print (sol.climbStairs(2))
print (sol.climbStairs(3))
print (sol.climbStairs(4))
print (sol.climbStairs(5))
print (sol.climbStairs(6))
print (sol.climbStairs(7))
print (sol.climbStairs(10))
print (sol.climbStairs(100))
