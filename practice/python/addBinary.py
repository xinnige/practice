class Solution(object):
    def toBinary(self, string):
        total = 0
        length = len(string)
        for i in range(length):
            total += (ord(string[i])-48)* 2**(length-i-1) 
        return total

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        string = bin(self.toBinary(a)+self.toBinary(b))[2:]
        return "0"*(max(len(a),len(b))-len(string))+string
        

sol = Solution()
#print sol.addBinary("11","1")
print sol.addBinary("100","101")
#print sol.addBinary("0101","01")
