# Create a list
numbers = [1, 2, 3, 4, 5]
print("Before swap:", numbers)

# Remember this pattern to swap:
# array[first], array[second] = array[second], array[first]
numbers[0], numbers[4] = numbers[4], numbers[0]

print("After swap:", numbers)

# Example 2: Swap middle numbers (2 and 4)
numbers[1], numbers[3] = numbers[3], numbers[1]
print("After swapping 2 and 4:", numbers)

# Example 3: Swap first and middle numbers
numbers[0], numbers[2] = numbers[2], numbers[0]
print("After swapping 1 and 3:", numbers)