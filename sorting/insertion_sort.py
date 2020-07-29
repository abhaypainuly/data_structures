def insertion_sort(unsorted):
    for i in range(1,len(unsorted)):
        j = i-1
        temp = unsorted[i]
        while j>=0 and unsorted[j]>temp:
            unsorted[j+1] = unsorted[j]
            j -= 1
        unsorted[j+1] = temp
    return unsorted