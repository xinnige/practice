class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        tail2 = n-1
        tail1 = m-1 
        if nums1[tail1] < nums2[tail2]:
            while nums1[tail1] < nums2[tail2]:
                 tail2 -= 1
            # nums2[tail2] < nums[tail1] < nums2[tail2+1]
            nums1[m+n-tail2-2:] = nums2[tail2+1:]
        print nums1


sol=Solution()
sol.merge([2,3,4,5,6],5,[1,7,8,9],4)

