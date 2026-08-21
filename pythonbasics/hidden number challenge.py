def find_threshold(target, low, high):

    while low <= high:
        mid = (low + high) // 2
        if mid == target:
            return mid
        if mid < target:
            low = mid + 1
        if mid > target: 
            high = mid - 1

    return None

numbers = [2, 5, 8, 12, 16, 21, 30]
find_threshold(numbers, 15)