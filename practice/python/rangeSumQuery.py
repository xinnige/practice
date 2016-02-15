class NumArray(object):
    def __init__(self, nums):
        self.length = len(nums)
        if self.length == 0:
            return
        self.sumArray = [0]*self.length
        self.sumArray[0] = nums[0]
        for i in range(self.length-1):
            self.sumArray[i+1] = self.sumArray[i] + nums[i+1]
        print self.sumArray

    def sumRange(self, i, j):
        if not hasattr(self, "sumArray"):
            return
        if i == 0:
            return self.sumArray[j]
        return self.sumArray[j] - self.sumArray[i-1]


if __name__ == "__main__":
    nums = []
    nums = [-2, 0, 3, -5, 2, -1]
    numArray = NumArray(nums)
    print numArray.sumRange(0, 2)
    print numArray.sumRange(2, 5)
    print numArray.sumRange(0, 5)
    

