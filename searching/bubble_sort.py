#BubbleSort
def bubble_sort(unsorted):
    l = len(unsorted) 
    for i in range(l-1):
        flag = True
        for j in range(l-i-1):
            if unsorted[j]>unsorted[j+1]:
                unsorted[j],unsorted[j+1] = unsorted[j+1],unsorted[j]
                flag = False
        if flag:
            break
    return unsorted