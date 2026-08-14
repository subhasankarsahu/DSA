def bubble_sort_optimised(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swapped = True
        
        if not swapped:
            break

    return arr

user_input = input("Enter numbers separated by spaces: ")

user_list = [int(x) for x in user_input.split()]

print(bubble_sort_optimised(user_list))