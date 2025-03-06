def find_minimum(numbers):
    if not numbers:  # Check if list is empty
        return None
    
    min_num = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
    return min_num

# Example usage
try:
    # You can change these numbers or get input from user
    a = [1, 2, 3, 4, 5]
    result = find_minimum(a)
    
    if result is not None:
        print(f"The minimum number in the list is: {result}")
    else:
        print("The list is empty!")
        
except Exception as e:
    print(f"An error occurred: {e}") 
