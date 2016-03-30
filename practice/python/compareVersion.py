class Solution(object):
    def is_zero(self, subarr):
        for i in subarr:
            if int(i) != 0:
                return False
        return True

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        minlength = min(len(arr1), len(arr2)) 
        for i in range(minlength):
            if int(arr1[i]) < int(arr2[i]):
                return -1
            if int(arr1[i]) > int(arr2[i]):
                return 1
            
        if len(arr1) > len(arr2):
            if self.is_zero(arr1[minlength:]):
                return 0
            return 1
        elif len(arr1) < len(arr2):
            if self.is_zero(arr2[minlength:]):
                return 0
            return -1
        return 0
        
        

sol = Solution()
print sol.compareVersion("1.2","1.0.3")
print sol.compareVersion("1.2","1.2.0")
print sol.compareVersion("1.2","1.2.0.00")
print sol.compareVersion("0.2.3","1.3")
print sol.compareVersion("1.0.3","1.0.3")
print sol.compareVersion("1.0.1","1.0")
