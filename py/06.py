a = [0] * 10
sum = 0
num = 0
average = 0
big = 0
for i in range(10):
    a[i] = float(input())
    sum += a[i]
    num += 1
average = (sum / num)

for i in range(10):
    if a[i] > average:
        big += 1
print(big)