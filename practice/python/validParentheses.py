class Solution(object):
    def isMatch(self, char1, char2):
        if char1 == "{" and char2 == "}":
            return True
        if char1 == "[" and char2 == "]":
            return True
        if char1 == "(" and char2 == ")":
            return True
        return False
     
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["{", "[", "("]
        right = ["}", "]", ")"]
        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) == 0:
                    return False
                if self.isMatch(stack[-1], char):
                    stack.pop()
                
        if len(stack) == 0:
            return True
        return False


sol = Solution()
print sol.isValid("")
print sol.isValid("()")
print sol.isValid("{}")
print sol.isValid("{[()]}")
print sol.isValid("[{]}")
