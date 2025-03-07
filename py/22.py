# Get the size of list
a = int(input("Enter how many numbers you want: "))
c = []  # Empty list to store numbers

# Get numbers from user
for i in range(a):
    num = int(input(f"Enter number {i+1}: "))
    c.append(num)  # Add the number to list

print("Your list:", c)

