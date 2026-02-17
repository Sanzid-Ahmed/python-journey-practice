def pivot_index(arr, low, high):
    pivot = arr[high]
    index = low - 1

    for i in range(low, high): 
        if arr[i] <= pivot:
            index+=1
            arr[i], arr[index] = arr[index], arr[i]
    
    arr[index + 1], arr[high] = arr[high], arr[index + 1]
    return index + 1



def quick_sort(arr, low, high):
    if low < high: 
        pivot_point = pivot_index(arr, low, high)

        quick_sort(arr, low, pivot_point - 1)
        quick_sort(arr, pivot_point + 1, high)

num = list(map(int, input("Enter the elements of the array: ").split()))
print("Original Array: ", num)

quick_sort(num, 0, len(num) - 1)
print("Sorted Array: ", num)