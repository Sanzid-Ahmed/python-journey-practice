def bubble_sort(arr):
    n = len(arr)

    for i in range(n): 

        for j in range(0, n - i - 1): 

            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



arr = list(map(int, input("Enter the values of the array: ").split()))

print("array: ", arr)

sorted_arr = bubble_sort(arr)

print("Sorted array: ", sorted_arr)


"""
input() → takes string
.split() → separates by space
map(int, ...) → converts each value to integer
list(...) → converts to list

"""