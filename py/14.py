num = int(input())
def fib(n):
    if n == 0:
        return 1
    else:
        return (num - 1) + (num - 2)
print(fib(num))

for i in range(fib(num)):
    print(i+1 , end = ' ')