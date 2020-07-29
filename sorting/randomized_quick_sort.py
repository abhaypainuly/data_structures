from random import randint

#RandomizedQuickSort

def randomized_partition(arr,low,high):
    
    #Function to arrange elements lesser than pivot to left side of piviot
    #pivot is random
    pivot = randint(low,high)
    arr[high],arr[pivot] = arr[pivot],arr[high]
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
    pIndex = randomized_partition(arr,low,high)
    quick_sort(arr,low,pIndex-1)
    quick_sort(arr,pIndex+1,high)