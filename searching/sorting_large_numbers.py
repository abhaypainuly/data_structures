#Sorting Large numbers while sorting
#Keeping in mind that large numbers are stored as strings

def compare(str1,str2):
    if len(str1)<len(str2):
        return True
    elif len(str1)>len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str2[i]<str1[i]:
                print(str1[i],str2[i])
                return False
            elif str2[i]>str1[i]:
                return True        
        return True

def mergeSort(arr):
    
    if len(arr)<2:
        print(arr)
        return arr

    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    
    L = mergeSort(L)
    R = mergeSort(R)

    i = k = j = 0
    
    while i<len(L) and j<len(R):
        if compare(L[i],R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i<len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j<len(R):
        arr[k] = R[j]
        j += 1
        k += 1    
    print(arr)
    return arr

def bigSorting(unsorted):
    unsorted = mergeSort(unsorted)    
    return unsorted



arr= '''1
2
100
12303479849857341718340192371
3084193741082937
3084193741082938
111
200'''
arr = arr.replace('\n',' ')
arr = arr.split()
print(arr)
#arr = [2,3,1,15,25324,16,25,2,6,614624774,457465422,2622626,0,26,235,32,85]
print(bigSorting(list(map(str,arr))))