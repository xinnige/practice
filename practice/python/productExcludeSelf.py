class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1] * len(nums)
        carrier = 1
        for i in range(1, len(nums)):
            carrier *= nums[i-1] 
            products[i] = carrier
        carrier = 1
        for j in reversed(range(len(nums))):
            products[j] *= carrier
            carrier *= nums[j]
        return products



sol = Solution()
print sol.productExceptSelf([1,2,3,4,3,2,1])
