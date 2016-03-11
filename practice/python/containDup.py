class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        idict = dict()
        for i in nums:
            if i in idict:
                return False
            idict[i] = None
        return True
        

sol = Solution()
print sol.containsDuplicate([])
print sol.containsDuplicate([1,2,3,4,5])
print sol.containsDuplicate([1,4,3,1,5])
