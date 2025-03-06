n = 5
m = 4
table = [[0] * m for i in range (n)]
for i in range(n):
    table[i] = list(map(int, input().split()))
print(table)