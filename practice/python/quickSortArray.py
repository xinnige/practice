def quickSort(arr, begin, end):
    i = begin
    j = end
    anchor = arr[begin]
    while i < j :
        while i < j and arr[j] > anchor:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] < anchor:
            i += 1
        arr[j] = arr[i]
    arr[i] = anchor

    if begin < i-1:
        quickSort(arr, begin, i-1)
    if end > i+1:
        quickSort(arr, i+1, end)

numbers = [2,5,4,1,7,9,3,8,0,6]
quickSort(numbers,0,len(numbers)-1)
print numbers
