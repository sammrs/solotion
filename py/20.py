a = [1, 2, 3, 4, 5]

# Method 1: Using reversed() function
print("Method 1 - Using reversed():")
for i in reversed(a):
    print(i)

# Method 2: Using negative indexing
print("\nMethod 2 - Using negative indexing:")
for i in range(len(a)-1, -1, -1):
    print(a[i])

# Method 3: Using slice with negative step
print("\nMethod 3 - Using slice:")
for i in a[::-1]:
    print(i)
    
