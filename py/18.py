# Write your code here
a = [1, 2, 3, 4, 5]

# Start coding with this list

# Method 1: Using min() function (simplest way)
print(f"Minimum number using min(): {min(a)}")

# Method 2: Using nested for loops
min_num = a[0]  # Start with first number
for i in range(len(a)):
    for j in range(len(a)):
        if a[j] < min_num:  # Compare each number with current minimum
            min_num = a[j]  # Update minimum if smaller number is found

print(f"Minimum number using nested loops: {min_num}")


