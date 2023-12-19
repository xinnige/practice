class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        array2D = []
        for i in range(nRows):
            array2D.append([])
        i = 0
        j = 0
        array2D[j].append(s[i])
        i += 1
        while i < len(s):
            j += 1
            while j < nRows and i < len(s):
                array2D[j].append(s[i])
                i += 1
                j += 1
            j -= 1
            while j > 0 and i < len(s):
                j -= 1
                array2D[j].append(s[i])   
                i += 1
        finalstr = ""
        for arr in array2D:
            onestr = "".join(arr)
            finalstr += onestr
        return finalstr

if __name__ == "__main__":
    sol = Solution()
    print (sol.convert("PAYPALISHIRING",3))
    print (sol.convert("PAYPALISHIRING",4))
    print (sol.convert("PAYPALISHIRING",2))
    print (sol.convert("PAYPALISHIRING",1))
