class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        array = [a for a in num]  
        array.sort()
        i = 0
        j = len(array)-1
        while i < j:
            result = array[i] + array[j]
            if result == target:
                break
            if result < target:
                i += 1
            else:
                j -= 1
        if i >= j:
            return -1,-1
        index1 = num.index(array[i])
        if array[i] == array[j]:
            index2 = num.index(array[j],i+1)
        else:
            index2 = num.index(array[j])
        if index1 > index2:
            return index2+1,index1+1
        return index1+1,index2+1

if __name__ == "__main__":
    sol = Solution()
    print sol.twoSum([2,7,11,15],9)
    print sol.twoSum([0,4,3,0],0)
    print sol.twoSum([5,75,25,100],100)
       
