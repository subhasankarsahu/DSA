def find_smallest(arr):
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num

    return smallest

arr = [1,2,3,4,5,6,7,8,9,0]

print(find_smallest(arr))