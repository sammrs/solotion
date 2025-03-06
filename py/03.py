a = list(map(int, input().split()))
sum = 0
for i in range(a):
    if int(a[i]) == 0:
        sum += 1
print(sum)