class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # calculate bulls
        bulls = 0
        totals = 0
        s_bases = [0]*10
        for s in secret:
            s_bases[ord(s)-48] += 1
        print s_bases

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

            s_bases[ord(guess[i])-48] -= 1
            if s_bases[ord(guess[i])-48] >= 0:
                totals += 1

        return "A%dB%d" % (bulls, totals-bulls)


sol = Solution()
print sol.getHint("1123","0111")
print sol.getHint("1708","7810")
print sol.getHint("1234","5678")
print sol.getHint("1111","1111")
