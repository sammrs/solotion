maxn = 100
counter = [0] * maxn

n = int(input())
xs = list(map(int, input().split()))

for x in xs:
    counter[x - 1] += 1

print(counter)