class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxvalue = max(nums)
        sumvalue = sum(nums)
        length = len(nums)
        # if lastonemissing
        if 0 not in nums:
            return 0
        expected = maxvalue*(length+1)/2-sumvalue
        if expected in nums:
            return maxvalue+1
        return expected

sol = Solution()
print sol.missingNumber([1,2,3,4,5])
print sol.missingNumber([0,1,2,4,5])
print sol.missingNumber([0,1,2,3,4])
print sol.missingNumber([0,2,3,4,5])
print sol.missingNumber([0,2])
