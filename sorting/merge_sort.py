#MergeSort
       
def merge_sort(arr):
    l = len(arr)
    if l==1:
        return
    #divinding array into two halfs
    L = arr[:l//2]
    R = arr[l//2:]
    
    #Sorting the divide halfs
    merge_sort(L)
    merge_sort(R)
    
    #merging sorted arrays
    i = j = k = 0    
    while i<(l//2) and j<(l-l//2):
        if L[i]<=R[j]:
            arr[k] = L[i]
            i += 1            
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i<(l//2):
        arr[k] = L[i]
        i += 1
        k += 1
    while j<(l-l//2):
        arr[k] = R[j]
        j += 1
        k += 1