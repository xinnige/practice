class Solution:
    # @param A, a list of integer
    # @return an integer
    def _singleNumber(self,A):
        number={}
        for i in A:
            if i in number:
                number[i] += 1
            else:
                number[i] = 1
        
        for key in number:
            if number[key] == 1:
                 return key


    def singleNumber(self,A):
        sum = 0
        for i in A:
            sum ^= i
        return sum

if __name__ == '__main__':
     sol = Solution()
     print sol.singleNumber([2,2,1,1,-3,3,3,4,4,5,5,6])
     print sol.singleNumber([1])
