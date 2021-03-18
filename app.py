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
