class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        summ = 0
        for index in range(len(s)):
            digit = ord(s[index]) - 64
            print "digit: ", digit
            print "index: ", index
            summ += 26 ** (len(s)-index-1) * digit
        return summ
        
        

if __name__ == "__main__":
    sol = Solution()
    # print "A", sol.titleToNumber("A")
    # print "C", sol.titleToNumber("C")
    # print "P", sol.titleToNumber("P")
    print "Z", sol.titleToNumber("Z")
    # print "AA", sol.titleToNumber("AA")
    # print "AB", sol.titleToNumber("AB")
    # print "BA", sol.titleToNumber("BA")
    # print "ZZ", sol.titleToNumber("ZZ")
