# Explanation: https://youtu.be/F1_KY1kaxIw
def quickSort(arr,start = 0, end = None):
    if(end == None):
        end = len(arr) - 1
    if(start < end):
        pivot = findPivot(arr,start,end)
    #print(pivot)
        quickSort(arr, start, pivot-1)
        quickSort(arr, pivot+1, end)
    return arr

    
    

def findPivot(arr,start,end):
    pivot = start
    key = arr[start]

    for i in range(start+1,end+1):
        if(key>arr[i]):
            pivot += 1
            arr[i],arr[pivot] = arr[pivot],arr[i]
    arr[start],arr[pivot] = arr[pivot],arr[start]
    return pivot

# print(quickSort([8,1,2,3,4,5,6,7]))
# print(quickSort([10,5,90,0,10]))

