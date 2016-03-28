from wrapper import func_wrapper

class Solution(object):
    @func_wrapper
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = len(nums) - 1
        head = 0
        while head < tail:
            if nums[head] == val:
                nums[head] = nums[tail]
                tail -= 1
                continue
            head += 1
        if head == 0:
            return head
        if nums[head] == val:
            return head
        return head + 1
        

sol = Solution()
sol.removeElement([3,2,2,3], 3)
sol.removeElement([], 3)
sol.removeElement([1], 1)
sol.removeElement([1,1,2,1,1,1], 1)
sol.removeElement([3,2,4,5,2,6,7], 2)

