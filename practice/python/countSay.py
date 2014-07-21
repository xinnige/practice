class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        previous_str = self.countAndSay(n-1)
        i = 0
        newstr = ""
        while i < len(previous_str):
            count = 1
            while i < len(previous_str)-1 and previous_str[i] == previous_str[i+1]:
                count += 1
                i += 1
            newstr += str(count)+previous_str[i]
            i += 1
        return newstr


if __name__ == "__main__":
    sol = Solution()
    print sol.countAndSay(2)
    print sol.countAndSay(3)
    print sol.countAndSay(4)
    print sol.countAndSay(5)
    print sol.countAndSay(6)
    print sol.countAndSay(7)
    print sol.countAndSay(8)
