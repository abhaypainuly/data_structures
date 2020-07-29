#Find 1st occurance of an element in the sorted list using Binary search
def binary_search_first(arr,end,x):
    start = 0
    end -= 1
    result = -1
    while start<=end:
        mid = (start+end)//2
        if x==arr[mid]:
            result = mid
            end = mid-1 
        elif x<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return result



#Find the last occurance of an element in a sorted list
def binary_search_last(arr,end,x):
    start = 0
    end -= 0
    result = -1
    while start<=end:
        mid = (start+end)//2
        if x==arr[mid]:
            result = mid
            start = mid+1
        elif x<arr[mid]:
            end = mid-1
        else:
            start = mid+1
    return result