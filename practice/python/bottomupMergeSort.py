def mergeSort(arr):
    length = 1
    length0 = len(arr)
    while length*2 < len(arr):
        i = 0
        while i < len(arr):
             newarr = merge(arr[i:i+length],arr[i+length:i+length*2])
             arr[i:min(i+2*length,length0)] = newarr[0:min(2*length,length0)]
             i += 2*length 
        length *= 2
    newarr = merge(arr[0:length],arr[length:])
    print newarr



def merge(arr1, arr2):
    i = 0
    j = 0
    newiter = 0
    newarr = [None]*(len(arr1)+len(arr2))
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newarr[newiter] = arr1[i]
            i += 1
            newiter += 1
        else:
            newarr[newiter] = arr2[j]
            j += 1
            newiter += 1
    while i < len(arr1):
        newarr[newiter] = arr1[i]
        i += 1
        newiter += 1
    while j < len(arr2):
        newarr[newiter] = arr2[j]
        j += 1
        newiter += 1
    return newarr
     
if __name__ == "__main__":
    mergeSort([1,5,4,3,8,7,9,2,6,])
    mergeSort([])
    mergeSort([2])
    mergeSort([4,2])
    mergeSort([4,2,4,6,2,3])
