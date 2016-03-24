class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        slist = list(secret)
        glist = list(guess)

        # calculate bulls
        bulls = 0
        for index in range(len(slist)):
            if slist[index] == glist[index]:
                bulls += 1
                slist[index] = None
                glist[index] = None
        
        print slist, glist
        # calculate cows
        cows = 0
        for index in range(len(glist)):
            if glist[index] is not None:
                if glist[index] in slist:
                    sindex = slist.index(glist[index])
                    slist[sindex] = None
                    cows += 1

        return "A%dB%d" % (bulls, cows)


sol = Solution()
print sol.getHint("1123","0111")
print sol.getHint("1708","7810")
print sol.getHint("1234","5678")
print sol.getHint("1111","1111")
