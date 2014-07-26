class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        rowindex = 0
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        if target >= matrix[rows-1][0]:
            rowindex = rows-1
        else: 
            rowindex = self.getRowth(matrix,target)
        if rowindex == -1:
            return False
        colindex =  self.binarySearch(matrix[rowindex],target)
        if colindex == -1:
            return False
        return True
    
    def getRowth(self,matrix,target):
        start = 0
        end = len(matrix)
        cols = len(matrix[0])-1
        while start < end:
           middle = (start+end)/2
           if start == end - 1:
               return start 
           if matrix[middle][0] > target:
               end = middle
           elif matrix[middle][cols-1] < target:
               start = middle
           else:
               return middle
        return -1
        

    def binarySearch(self, array, target):
        start = 0
        end = len(array)
        if end == 0:
            return -1
        if array[0] == target:
            return 0
        if array[end-1] == target:
            return end-1
        if end == 1:
            if array[0] == target:
                return 0
            else:
                return -1
        while start < end:
            middle = (start + end)/2
            if array[middle] == target:
                return middle
            if array[middle] > target:       
                end = min(middle,end-1)
            else:
                start = max(middle,start+1)
        return -1

if __name__ == "__main__":
    sol = Solution()
    matrix = [
                [1,3,5,7,8,],
                [10,11,16,20,21,],
                [23,30,34,50,60,],
             ]
    matrix = [[1],[3]]
    target = 2
    print sol.searchMatrix(matrix,target)
