# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    # 5 is the first bad version
    print "call for ", version
    if version >= 5:
        return True
    return False

class Solution(object):
    def __init__(self):
        self.searchmap = dict()

    def binarySearch(self, start, end):
        """
        :type n: int
        :rtype: int
        """
        half = start + (end - start)/2
        if isBadVersion(half):
            if not isBadVersion(half-1):
                return half
            return self.binarySearch(start, half-1)
        else:
            if isBadVersion(half+1):
                return half+1
            return self.binarySearch(half+1, end)
                
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binarySearch(1, n)
        

sol = Solution()
print sol.firstBadVersion(108)
