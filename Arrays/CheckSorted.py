# def isSorted(arr):
#     for i in range(len(arr) - 1):
#         if arr[i] >= arr[i+1]:
#             return False

#     return True

# arr = [1, 2, 5, 8]
# print(isSorted(arr))

arr = [1, 2, 5, 8]

isSorted = all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))

print(isSorted)