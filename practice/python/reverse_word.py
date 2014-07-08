class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        strarr = s.strip().split(" ");
        mystr = ""
        myrange = range(len(strarr))
        for i in myrange[::-1]:
            if strarr[i] == "":
                continue
            mystr += strarr[i]+' '
        return mystr[:-1]

if __name__ == '__main__':
    sol = Solution()
    print sol.reverseWords('the sky is blue') 
    print sol.reverseWords('  the sky is blue  ') 
    print sol.reverseWords('  the    sky   is   blue  ') 
