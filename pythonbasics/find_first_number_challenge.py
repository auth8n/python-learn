def find_threshold(numbers, target):
    low = 0
    high = len(numbers)-1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] < target: 
            low = mid + 1
        else: 
            high = mid - 1
            
    if low < len(numbers):
        return numbers[low]
    
    return None

numbers = [2, 5, 8, 12, 16, 21, 30]
print(find_threshold(numbers, 29))

