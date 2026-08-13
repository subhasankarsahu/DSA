n = int(input("Enter the no of elements: "))

arr = []

for i in range(n):
    arr.append(int(input()))
        
for i in range(n):
    mini = i

    for j in range(i+1, n):
        if(arr[j]<arr[mini]):
            mini = j

        arr[i], arr[mini] = arr[mini], arr[i]

print("Sorted array: ")
print(arr)