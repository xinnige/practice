class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self,s):
        if len(s) == 0:
            return True
        i = 0
        j = len(s)-i-1
        while i < len(s) and j >= 0 and i<=j:
            if not s[i].isalpha() and not s[i].isdigit():
                i += 1
                continue
            if not s[j].isalpha() and not s[j].isdigit():
                j -= 1
                continue
            if s[j].lower() != s[i].lower():
                return False
            i += 1
            j -= 1
        return True
            
if __name__ == '__main__':
    sol = Solution()
    print sol.isPalindrome("A man, a plan, a canal: Panama")
    print sol.isPalindrome("race a car.")
    print sol.isPalindrome("")
    print sol.isPalindrome("12345")
    print sol.isPalindrome("123 21")
    print sol.isPalindrome("v' 5:UxU:5 v'")
