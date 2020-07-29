#Finding no of rotation in a circularly sorted array if there are no dublicates in the array
def no_of_rotation(arr,l):
    low = 0
    high = l-1    
    while low<=high:
        if arr[low]<=arr[high]:
            return low
        mid = (low+high)//2
        if arr[(mid+l-1)%l]>=arr[mid]<=arr[(mid+1)%l]:
            return mid
        elif arr[mid]<=arr[high]:
            high = mid-1
        elif arr[low]<=arr[mid]:
                low = mid+1 
    return -1