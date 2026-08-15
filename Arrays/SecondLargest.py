def secondLargest(arr):
    largest = arr[0]
    sLargest = -1 

    for i in range(len(arr)):
        if arr[i] > largest:
            sLargest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > sLargest:
            sLargest = arr[i]

    return sLargest

arr = [5, 1, 2, 7, 3, 7]
print(secondLargest(arr))