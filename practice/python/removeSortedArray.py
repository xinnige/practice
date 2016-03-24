class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pointer = 0
        npointer = pointer + 1
        while pointer < len(nums) and npointer < len(nums):
            if nums[pointer] == nums[npointer]:
                npointer += 1 
            else:
               if npointer > pointer + 1:
                   nums[pointer+1] = nums[npointer]
               pointer += 1
               npointer += 1
        print nums[:pointer+1]     
        return pointer + 1
        

sol = Solution()
print sol.removeDuplicates([])
print sol.removeDuplicates([0])
print sol.removeDuplicates([0,0,0])
print sol.removeDuplicates([0,1])
print sol.removeDuplicates([0,1,1,1,2,3,4,4,5,6,7,8,8,8,9])
print sol.removeDuplicates([0,0,0,1,1,1,2,3,4,4,5,6,7,8,8,8,9,9])

