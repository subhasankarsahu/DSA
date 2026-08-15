def largestElement(arr):
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest

arr = [5, 1, 3, 7, 4, 2]
print(largestElement(arr))