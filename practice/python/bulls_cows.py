class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        # calculate bulls
        bulls = 0
        s_bases = [0]*10
        g_bases = [0]*10
        for index in range(len(secret)):
            if secret[index] == guess[index]:
                bulls += 1
            else:
                s_bases[ord(secret[index])-48] += 1        
                g_bases[ord(guess[index])-48] += 1        
        
        # calculate cows
        cows = sum(map(min,zip(s_bases, g_bases)))

        return "%dA%dB" % (bulls, cows)


sol = Solution()
print sol.getHint("1123","0111")
print sol.getHint("1708","7810")
print sol.getHint("1234","5678")
print sol.getHint("1111","1111")
