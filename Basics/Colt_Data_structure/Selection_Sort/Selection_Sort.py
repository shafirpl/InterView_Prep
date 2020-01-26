def selection_sort(arr):
    length = len(arr)
    if (length <= 1): return arr
    for i in range(length-1):
        minIndex = i
        for j in range(i+1,length):
            if(arr[minIndex]>=arr[j]):
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex], arr[i]
    return arr

