import wrapper

class Solution(object):
    @wrapper.func_wrapper
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 0:
            return
        temp = nums[0:3]
        for i in range(length):
            index = (i + k) % length
            nums[i] = nums[index]
        nums[length-3:length] = temp
        nums[]


sol = Solution()
# sol.rotate([], 3)
# sol.rotate([1], 3)
sol.rotate([1,2], 3)
# sol.rotate([1,2,3], 3)
# sol.rotate([1,2,3,4,5,6,7] ,3)
