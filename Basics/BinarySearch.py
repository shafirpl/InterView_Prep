# TLDR: Don't Include the middle point, we don't need to include
# middle point as we already checked it against something


def binary_search_recursive(arr,num,start = 0, end = 0, endFlag = True):
    length = len(arr)
    if (length == 0): return -1
    if (endFlag): end = length - 1
    middle = (start+end)//2
    if(arr[middle] == num): return middle
    elif(start > end): return -1
    else:
        if(num>arr[middle]): return binary_search_recursive(arr,num,middle+1,end,False)
        else: return binary_search_recursive(arr,num,start,middle-1,False)

def binary_search_iterative(arr,num):
    start = 0
    end = len(arr) - 1
    if( len(arr) == 0): return -1
    middle = (start + end) // 2
    if (arr[middle] == num): return middle

    while(start <= end):
        if(num> arr[middle]):
            start = middle + 1
            middle = start + end // 2
        elif(num == arr[middle]): 
            return middle
        else:
            end = middle - 1
            middle = (start + middle) //2
    return -1

