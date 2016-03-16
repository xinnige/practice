import wrapper
class Solution(object):
    def __init__(self):
        self.results = {}
 
    def isHappy2(self, n):
        while n != 1:
            sum = 0
            num = n
            while num > 0:
                sum = sum + (num%10) ** 2
                num = num/10;
            
            n = sum
            if n < 10 and n != 1:
                return False
        return True
 
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        if n in self.results:
             return False
        self.results[n] = None
        nstr = str(n)
        for c in nstr:
            result += int(c) ** 2
        if result == 1:
            return True
        return self.isHappy(result)   


sol = Solution()
print sol.isHappy(19)
print sol.isHappy(0)
print sol.isHappy(2)


