def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        #let us find the minimum value first
        min_index = i

        #now lets look at the remaining partition of unsorted items
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [34, 546, 75, 7868, 8, 83, 2, 4]
print(selection_sort(arr))