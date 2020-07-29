#Binay Search
def binary_search(arr,x):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if x==arr[mid]:
            return mid
        elif x<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return -1


#Recursive Binary Search
def binary_search(arr,start,end,x):
    if start>end:
        return -1
    mid = (start+end)//2
    if x==arr[mid]:
        return mid
    elif x<arr[mid]:
        return binary_search(arr,start,mid-1,x)
    else:
        return binary_search(arr,mid+1,end,x)