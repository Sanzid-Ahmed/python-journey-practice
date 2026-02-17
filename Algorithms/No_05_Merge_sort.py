def merge(arr, low, mid, high):
    left = arr[low : mid + 1]
    right = arr[mid + 1: high + 1]

    i = 0
    j = 0
    k = low

    while i < len(left) and j < len(right): 
        if left[i] <= right[j]: 
            arr[k] = left[i]
            i += 1
        else: 
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right): 
        arr[k] = right[j]
        k += 1
        j += 1



def merge_sort(arr, low, high): 
    if low < high: 
        # // → integer division
        mid = low + (high - low)// 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)

        merge(arr, low, mid, high)


num = list(map(int, input("Enter the elements of the array: ").split()))
print("Original Array: ", num)

merge_sort(num, 0, len(num) - 1)
print("Sorted Array: ", num)