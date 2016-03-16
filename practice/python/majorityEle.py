class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = None
        count = 0
        for num in nums:
            if count == 0:
                major = num
            if major == num:
                count += 1
            else:
                count -= 1
        return major

sol = Solution()
print sol.majorityElement([1])
print sol.majorityElement([1,1,2])
print sol.majorityElement([1,2,3,4,5,3,3,3,3,3])
