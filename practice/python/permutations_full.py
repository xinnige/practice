class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if num == 1:
            return [[1]]
        permutelist = []
        array = self.permute(num-1)
        for arr in array:
            for i in range(len(arr)+1):
                permutelist.append(self.insertarray(arr,i,num)) 
        return permutelist 

    def insertarray(self,arr,index,item):
        newarr = [i for i in arr]
        newarr.insert(index,item)
        return newarr


if __name__ == "__main__":
    sol = Solution()
    print len(sol.permute(5))
