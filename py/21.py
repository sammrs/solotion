# Write your code here
a = [1, 2, 3, 4, 5]
print("Original array:", a)

# Bubble sort in ascending order (smallest to largest)
n = len(a)
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:    # Change < to > for ascending order
            # Swap the elements
            a[i], a[j] = a[j], a[i]

print("Sorted array (ascending):", a)


