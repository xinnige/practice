class Solution(object):
    def __init__(self):
        self.rob_map = None

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.rob_map = [0]*len(nums)
        for index in range( len(nums)):
            if index == 0:
                self.rob_map[0] = nums[0]
            elif index == 1:
                self.rob_map[1] = max(self.rob_map[0], nums[1])
            else:
                self.rob_map[index] = max(self.rob_map[index-1], self.rob_map[index-2]+nums[index])
        return self.rob_map[-1]


sol = Solution()
print sol.rob([10,8,9,4,6,12,39,2])


