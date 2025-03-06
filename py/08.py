n, x = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(x):
    t = nums[n - 1]
    for j in range(n - 1, 0, -1):
        nums[j] = nums[j - 1]
    nums[0] = t

for number in nums:
    print(number, end = ' ')