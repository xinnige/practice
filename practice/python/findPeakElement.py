class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[-1] > nums[-2]:
            return nums[-1]
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i+1] and nums[i] > nums[i-1]:
                return nums[i]


sol = Solution()
print sol.findPeakElement([])
print sol.findPeakElement([1])
print sol.findPeakElement([1,0,1,2])
print sol.findPeakElement([1,2,3])
print sol.findPeakElement([1,2,3,1])
