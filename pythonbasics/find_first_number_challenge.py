def find_threshold(numbers, target):
    low = 0
    high = len(numbers)-1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] >= target:
            high = mid - 1
            #Check if it is equal to the target
            if numbers[mid] == target:
                return numbers[mid]
            elif target > numbers[mid-1] and target < numbers[mid]:
                return numbers[mid]
                
            #Check to see if its the last iteration
            if numbers[low] == numbers[high-1]:
                if target < numbers[mid]:
                    return numbers[mid]
                else:
                    return numbers[mid+1]

            #Check now for limits
            if target <= numbers[0]:
                return numbers[0]
            if target > numbers[high]:
                return "Out of bound"
    
        if numbers[mid] < target:
            low = mid + 1 
            #Check if it is equal to the target
            if numbers[mid] == target:
                return numbers[mid]
            elif target > numbers[mid-1] and target < numbers[mid]:
                return numbers[mid]
            
            #Check to see if its the last iteration
            if numbers[low] == numbers[high-1]:
                if target < numbers[mid]:
                    return numbers[mid]
                else:
                    return numbers[mid+1]

            #Check now for limits
            if target <= numbers[0]:
                return numbers[0]
            if target > numbers[high]:
                return "Out of bound"

    return None

numbers = [2, 5, 8, 12, 16, 21, 30]
print(find_threshold(numbers, 40))

