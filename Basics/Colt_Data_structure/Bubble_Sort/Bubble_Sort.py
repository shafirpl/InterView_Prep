def bubble_sort(arr):
    length = len(arr)
    if(length == 0): return arr
    # it goes like this, after first loop, first highest number at the 
    # end of the loop, and so on, so if we have 5 numbers, after first loop
    # 14 will be at the end of the array, afrer 2nd loop second highest number
    # 10 will be at the second end of the array and so on, so after fourth loop, 
    # the fourth highest number will be at the end which means we don't need
    # to run another loop, becuase after 4th loop all the 4 highest numbers
    # are already sorted, which means the 5th number is sorted. So we need 4 loops,
    # or loop from 0 to 3. So it is length - 2, since range exclude the last number
    # for example range(5) will give us 0 to 4, we do range(length-1)
    # https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/learn/lecture/11071950#questions
    # watch this video for the swap thing
    for i in range(length-1):
        j = 0
        noSwap = True
        while (j< length - i):
            if(j+1 < length and arr[j+1] <= arr[j]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
                noSwap = False
            j += 1
        if (noSwap): break

    return arr

print(bubble_sort([14,5,8,2,10]))