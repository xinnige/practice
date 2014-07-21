class Solution:
    # @return a list of integers
    def grayCode(self, n):
       codearray = []
       strlist = self._grayCode(n)
       for c in strlist:
          codearray.append(self._convert(c))
       return codearray

    def _grayCode(self, n):
       if n == 0:
           return []
       if n == 1:
           return ["0","1"]
       previouslist = self._grayCode(n-1)
       newlist = []
       for c in previouslist:
           newlist.append("0"+c)
       for i in range(len(previouslist),0,-1):
           newlist.append("1"+previouslist[i-1])
       return newlist

    def _convert(self, code):
       number = 0
       for i in range(len(code)):
           number += int(code[i])*(2**(len(code)-1-i))
       return number  

if __name__ == "__main__":
    sol = Solution()
    print sol.grayCode(2)
    print sol.grayCode(0)
    print sol.grayCode(2)
    print sol.grayCode(3)
