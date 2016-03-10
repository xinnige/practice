class Solution(object):
    def moveZeroes(self, nums):
        tail = 0  #points to 1 past the last non-zero entry
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            tail += 1
            if i != 0:
                nums[tail-1] = nums [i] #//Overwrite since there are 0s in the middle
                nums[i] = 0

    def moveZeroes2(self, nums):
        tails = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tails += 1
                continue
            tmp = nums[i - tails]
            nums[i - tails] = nums[i]
            nums[i] = tmp

    def moveZeroes_succeed( self, nums):
        current = 0
        index0 = -1
        while current < len(nums):
            if nums[current] == 0:
                if index0 == -1:
                    index0 = current
                current += 1
                continue
            # hit a non-zero element
            if index0 != -1:
                nums[index0] = nums[current]
                index0 += 1
            current += 1
        if index0 == -1:
            return
        for i in range(index0, current):
            nums[i] = 0
        
        
    def moveZeroes_timeout(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current = 0
        step = 0
        while current < len(nums):
            if nums[current] == 0:
                step = step + 1
            elif step != 0:
                # hit a non-zero element
                nums[current - step] = nums[current]
                nums[current] = 0
                step = 0
                current =- step
            current += 1

def action(sol, nums):
    print nums, "->",
    sol.moveZeroes(nums)
    print nums

if __name__ == "__main__":
    sol = Solution()
    action(sol, [0,1,0,2,0,3,0,4,0,5])
    action(sol, [0,1,2,3,4,5,6,7])
    action(sol, [])
    action(sol,[0])
    action(sol,[1])
    action(sol,[1,2,3])
    action(sol,[1,2,3,0])
    action(sol,[1,2,0,0,3,4,0,0,0,0,0,5,0])
    action(sol,[1,2,3,4,5,0,0,0,0,0])
    action(sol,[0,4,2,3,1,1,0,9,0,0,0])
