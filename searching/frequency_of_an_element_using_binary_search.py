#Finding the frequency of an element in a sorted list using binary search algorithm
def frequency(arr,l,x):    
    def binary_search(arr,high,x,first):
        low = 0
        high -= 1
        result = -1
        while low<=high:
            mid = (low+high)//2
            if x==arr[mid]:
                result = mid
                if first:
                    high = mid-1
                else:
                    low = mid+1
            elif x<arr[mid]:
                high = mid-1
            else:
                low = mid+1
        return result
    
    result = binary_search(arr,l,x,True)
    if result==-1:
        return 0
    else:
        return binary_search(arr,l,x,False)-result+1