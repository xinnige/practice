class Solution:
    def match(self, haystack:str, needle:str, iH:int, iN:int) -> bool:
        while iN < len(needle) and iH < len(haystack) and haystack[iH] == needle[iN]:
            iH += 1
            iN += 1
        if iN == len(needle) and haystack[iH-1] == needle[iN-1]:
            return True
        return False

    def strStr(self, haystack: str, needle: str) -> int:
        for j in range (len(haystack)):
            if haystack[j] == needle[0]:
                if self.match(haystack, needle, j,0):
                    return j
        return -1
    
if __name__=="__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad","sad"))
    print(sol.strStr("leetcode","leeto"))
    print(sol.strStr("leetcode","code"))