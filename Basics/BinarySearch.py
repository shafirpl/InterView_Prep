def binary_search(arr,num):
    length = len(arr)
    if (length == 0): return False
    start = 0
    end = len(arr) - 1
    middle = (start+end)//2
    # if(length % 2 != 0): middle += 1
    if(arr[middle] == num): 
        return True
    elif (len(arr) <= 1): return False
    else:
        if(num>arr[middle]): return binary_search(arr[middle+1:],num)
        else: return binary_search(arr[:middle],num)

def binary_search_index(arr,num,start = 0, end = 0, endFlag = True):
    length = len(arr)
    if (length == 0): return -1
    if (endFlag): end = length - 1
    middle = (start+end)//2
    if(arr[middle] == num): return middle
    elif(start > end): return -1
    else:
        if(num>arr[middle]): return binary_search_index(arr,num,middle+1,end,False)
        else: return binary_search_index(arr,num,start,middle-1,False)

def binary_search_iter(arr,num):
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

#print(binary_search_iter([1,2,3,4],1))


# arr = [1,2,3,4]
# print(binary_search(arr,3))