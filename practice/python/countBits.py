class Solution(object):
    def _fill(self, bits, period):
        """
        fill the [period, period*2-1]
		"""
        half_period = period/2
        bits += bits[half_period:period]
        bits += [ (i+1) for i in bits[period/2:period]]

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0,1,1,2,1,2,2,3]
        period = 4
        while period*2 <= num:
            period *= 2
            self._fill(bits, period)
        return bits[:(num+1)]

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0]
        period = 1
        pointer = 0
        for i in range(1, num+1):
            bits.append( bits[i-period]+1 ) 
            pointer += 1
            if pointer == period:
                period *= 2
                pointer = 0
        return bits

    def slowCountBits(self, num):
        for i in range(num+1):
            bits = self._countSingle(i)
            print bits,
    
    def _countSingle(self, num):
        count = 0
        while num != 0:
            num &= num -1
            count += 1
        return count


sol = Solution()

print 4, sol.countBits(4)
print 8, sol.countBits(8)
print 16, sol.countBits(16)
print 31, sol.countBits(31)
print 32, sol.countBits(32)
print 33, sol.countBits(33)

