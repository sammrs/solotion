# Write your code here
a = [1, 2, 3, 4, 5]

# Start coding with this list
n = len(a)
for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)


