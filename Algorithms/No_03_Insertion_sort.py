def Insertion_sort(arr): 
    size = len(arr)

    for i in range(1, size):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key: 
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    
    return arr

num = list(map(int, input("Enter the elements of the array: ").split()))
print("Original Array: ", num)

numbers = Insertion_sort(num)
print("Sorted Array: ", numbers)