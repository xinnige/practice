class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        # length dict with the format as:
        # key: left value
        # value: max length
        # so the right size should be leftvalue+maxlength-1
        rangedict = {}
        if num is None or len(num) == 0:
            return 0;
        for i in num:
            low = i
            high = i
            if i in rangedict:
               continue
            if i+1 in rangedict:
                high = rangedict[i+1]
            if i-1 in rangedict:
                low = rangedict[i-1]
            rangedict[i] = i
            rangedict[low] = high
            rangedict[high] = low
            print i
            print rangedict
        return max([abs(key-value)+1 for key,value in rangedict.items()])

            
               
if __name__ == '__main__':
    sol = Solution()
    #print sol.longestConsecutive([-2,-3,7,5,0,-8,-4,-1,2])
    print sol.longestConsecutive([-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2])
    #print sol.longestConsecutive([100,200,4,3,1,2,0,-1])
