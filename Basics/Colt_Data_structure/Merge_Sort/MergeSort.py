def mergeSort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    left = mergeSort(arr[0:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def merge(arr1,arr2):
    result = []
    i,j = 0,0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j+= 1
    
    if(i<j):
        for k in range(i,len(arr1)):
            result.append(arr1[k])
    
    else:
        for k in range(j,len(arr2)):
            result.append(arr2[k])

    return result

print(mergeSort([1,2,3,4,5,6]))
print(mergeSort([1,4,6,2,2,3,5,7]))
print(mergeSort([100,200,1,2,3,5,6]))
