#SelectionSort
def selection_sort(unsorted):
    l = len(unsorted)
    for i in range(l-1):
        mini_index = i
        for j in range(i+1,l):
            if unsorted[j]<unsorted[mini_index]:
                mini_index = j
        if mini_index !=i:
            unsorted[i],unsorted[mini_index] = unsorted[mini_index],unsorted[i]
    return unsorted