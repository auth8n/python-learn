def approximate_square_root(number, tolerance):
    if number < 0:
        raise ValueError("Square root of a negative number is not defined in real numbers")

    if number == 0 or number == 1:
        return f"The square root of {number} is approximately {number}"

    low = 0
    high = max(1, number) #use 1 as default else the number passed

    while (high - low) > tolerance:
        mid = (low + high) / 2 #calculate the midpoint

        #if the value is approximately similar to the number
        if high - low <= tolerance:
            return mid

        #a check to see if our square is getting closer to the number so that we can return it
        if mid ** 2 < number:
            low = mid 
        else:
            high = mid 

    return None
print(approximate_square_root(2, 0.01))