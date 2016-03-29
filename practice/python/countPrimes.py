class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n -= 1
        primes = [1]*n
        if n > 0:
            primes[0] = 0
        for index in range(1, int(n**0.5)):
            if primes[index] == 0:
                continue 
            maker = index + 1
            multiplier = maker 
            while maker*multiplier <= n:
                primes [maker*multiplier-1] = 0
                multiplier += 1
        return sum(primes)
        

sol = Solution()
for i in range(50):
    print i, sol.countPrimes(i)
print 139, sol.countPrimes(139)
