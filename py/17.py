a = [1, 2, 3, 4, 5]
n = len(a)
min_num = a[0]  # Initialize with first number
for i in range(n):
    if a[i] < min_num:  # If current number is smaller than min_num
        min_num = a[i]  # Update min_num with the smaller number

print(f"The minimum number in the list is: {min_num}") 
