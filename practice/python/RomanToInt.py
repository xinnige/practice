class Solution:
    # @return an integer
    def romanToInt(self, s):
       lastmax = 0
       symbolmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
       result  = 0 
       for c in s[::-1]:
           current = symbolmap[c]
           if current == lastmax:
               result += current
           elif current > lastmax:
               result += current
               lastmax = current
           else:
               result -= current
       return result 

    






if __name__ == "__main__":
    sol = Solution()
    print sol.romanToInt("MMXIV"), 2014
    print sol.romanToInt("II"), 2
    print sol.romanToInt("XIII"), 13
    print sol.romanToInt("CCVII"), 207
    print sol.romanToInt("MLXVI"), 1066
    print sol.romanToInt("MCMIV"), 1904
    print sol.romanToInt("MCMLIV"), 1954
    print sol.romanToInt("MCMXC"), 1900
