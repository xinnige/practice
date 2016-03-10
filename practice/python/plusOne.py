class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        print digits,
        result = []
        carrier = 1
        for digit in digits[::-1]:
            result.append( (int(digit) + carrier) % 10)
            carrier = ( int(digit) + carrier) / 10
        if carrier > 0:
            result.append(carrier)
        return result[::-1]
        

if __name__ == "__main__":
    sol = Solution()
    print sol.plusOne([0])
    print sol.plusOne([9])
    print sol.plusOne([9,9])
    print sol.plusOne([9,9,9])
    print sol.plusOne([1,1,1,1])
    print sol.plusOne([6,5,5,3,5])
