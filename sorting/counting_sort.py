#Counting Sort

def counting_sort(arr):
    l=0
    maxi = None
    
    #Calculating lenght and finding maximum simulanioustly 
    for val in arr:
        if maxi is None:
            maxi = val
        elif val>maxi:
            maxi = val
        l += 1
    
    lst = [0]*(maxi+1)
    #Counting occurance of each element
    for val in arr:
        lst[val] += 1
    
    count = 0
    prev = 0
    #converting count to 'starting indices' of every element by adding all elements occured before the element 
    for i in range(maxi+1):
        lst[i],count = count,count+lst[i]
            
    new_arr = [0]*l 
    for i in range(l):
        new_arr[lst[arr[i]]] = arr[i]
        lst[arr[i]] += 1
    
    return new_arr