def bubble_sort(arr): #O(n**2)
    n = len(arr)
    for i in range(n):
       # this is the number of loops we do
        for j in range(0, n-i-1):
            # arr[j]  compared to arr[j+1]
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([1,4,5,6,3]))


def insertion_sort(arr):
    operations = 0
    for i in range(len(arr)):
        num_we_are_on = arr[i]
        j = i-1 # j = -1
        # do a check to see that we dont go out of range
        while j >= 0 and arr[j] > num_we_are_on:
            operations += 1
            # this check will be good, because we won't check arr[-1]
            arr[j+1] = arr[j]  # move larger number forward
            j -= 1
        j += 1
        arr[j] = num_we_are_on
    return arr, operations

test_arr = [3,5,3,7,2,6,3,4,1]
ordered_array, operations = insertion_sort(test_arr)
print(ordered_array, operations)
