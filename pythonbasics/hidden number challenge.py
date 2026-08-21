def find_number(target, low, high):

    while low <= high:
        mid = (low + high) // 2
        if mid == target:
            return mid
        if mid < target:
            low = mid + 1
        if mid > target: 
            high = mid - 1

    return None
