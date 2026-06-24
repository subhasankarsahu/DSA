def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [1,2,3,4,5,6,7,8,9,0]

print(find_largest(arr))

