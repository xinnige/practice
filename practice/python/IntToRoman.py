class Solution:
    # @return a string
    def intToRoman(self, num):
       numstr = ""
       symbolarray = [("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
       for c,i in symbolarray[::-1]:
           while num - i >= 0:
               num -= i
               numstr += c
       prechar = None 
       counter = 0 
       index = 0
       result  = ""
       for c in numstr[::-1]:
           prechange = False
           print symbolarray[index][0], c, prechar 
           if prechar is None:
               counter += 1
           if prechar is not None:
               if prechar == c:
                   counter += 1
                   if counter * symbolarray[index][1] == symbolarray[index+1]:
                       result = result[:0-counter]
                       result = symbolarray[index+1][0] + result
                       prechange = True
                   if counter == 4:
                       result = result[:0-counter]
                       result = c+symbolarray[index+1][0] + result
                       prechange = True
               else:
                   counter = 0
                   #TODO
                   index += 1
                   if index == len(symbolarray):
                      break
           if not prechange:
               prechar = c
               result = c + result

       return numstr,result
        
if __name__ == "__main__":
    sol = Solution()
    print sol.intToRoman(2014),"MMXIV"
    print sol.intToRoman(2),"II"
    print sol.intToRoman(13),"XIII" 
    print sol.intToRoman(207),"CCVII"
    print sol.intToRoman(1066),"MLXVI"
    print sol.intToRoman(1904),"MCMIV"
    print sol.intToRoman(1954),"MCMLIV"
    print sol.intToRoman(1900),"MDCD"
    print sol.intToRoman(1990),"MCMXC"
