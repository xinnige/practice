class Solution(object):
    def get_majority(self, n, factor):
        power = factor
        shang = n/power
        counter = shang
        while shang > 0:
            power = power*factor   
            shang = n/power
            counter += shang
        return counter 
        
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num5 = self.get_majority(n, 5)
        num2 = self.get_majority(n, 2)
        print num5
        return min(num5, num2)

sol = Solution()
print sol.trailingZeroes(1)
print sol.trailingZeroes(20)
print sol.trailingZeroes(100)        

