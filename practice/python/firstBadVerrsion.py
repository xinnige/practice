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
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) / 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
print sol.firstBadVersion(108)
