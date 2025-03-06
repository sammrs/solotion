import time

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

start_time = time.time()

fib(20)

end_time = time.time()

print(end_time - start_time)