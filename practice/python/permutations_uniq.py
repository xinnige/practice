class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 1:
            return [num]
        array = self.permute(num[:-1])
        item = num[-1]
        permutedict = {}
        for arr in array:
            for i in range(len(arr)+1):
                newarr = self.insertarray(arr,i,item)
                newarrstr = ",".join([str(i) for i in newarr])
                if newarrstr not in permutedict:
                    permutedict[newarrstr] = 1
        permutelist = []
        for arrstr in permutedict.keys():
            strlist = arrstr.split(",")
            permutelist.append([int(s) for s in strlist])
        return permutelist

    def insertarray(self,arr,index,item):
        newarr = [i for i in arr]
        newarr.insert(index,item)
        return newarr

if __name__ == "__main__":
    sol = Solution()
    print sol.permute([1,1,2])
    print sol.permute([1,])
    print sol.permute([1,2,2,3,3])
