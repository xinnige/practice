def merge(arr1, arr2):
    i = 0
    j = 0
    newarr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            newarr.append(arr1[i])
            i += 1
        else:
            newarr.append(arr2[j])
            j += 1
        
    if j < len(arr2):
        newarr.extend(arr2[j:])
    if i < len(arr1):
        newarr.extend(arr1[i:])
    return newarr


def mergeSort(arr):
    length = len(arr)
    if length <= 1:
        return arr   
    return merge(mergeSort(arr[0:length/2]),mergeSort(arr[length/2:]))


if __name__ == "__main__":
    print mergeSort([9,3,5,2,8,7,6,1,0,4,11,10,20])
    print mergeSort([])

