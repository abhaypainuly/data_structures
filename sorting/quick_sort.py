#QuickSort
def partition(arr,low,high):
    
    #Function to arrange elements lesser than pivot to left side of piviot
    #pivot is always end
    pIndex = i = low
    while i< high:
        if arr[i]<=arr[high]:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex += 1
        i += 1
    arr[high],arr[pIndex] = arr[pIndex],arr[high]
    return pIndex

def quick_sort(arr,low,high):
    if low>=high:
        return
    pIndex = partition(arr,low,high)
    quick_sort(arr,low,pIndex-1)
    quick_sort(arr,pIndex+1,high)