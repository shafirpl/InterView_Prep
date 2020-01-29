# Think of it as a hole/black box moving
# In the outer loop, we pick up the hole, and
# then in the inner array we move the hole to appropriate position
# and then in outer array we set the hole to the actual value
# Since we assume the first value is sorted, we start i at 1
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while(j>=0 and arr[j]>=key):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    return arr

# print(insertion_sort([1,0,3,5,1,5,0,2]))
