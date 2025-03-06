m = 3
n = 2
table = [[0] * m for i in range (n)]
for i in range(n):
    table[i] = list(map(int, input().split()))

n = len(table) # number of rows
m = len(table[0]) # number of columns

print(table)

for i in range(n):
    for j in range(m):
        print(table[i][j], end= " ")
    print()