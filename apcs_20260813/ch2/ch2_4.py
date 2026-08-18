import time

def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib_rec(n-2) + fib_rec(n-1)
start = time.time()
ans = fib_rec(37)
end = time.time()

print(ans)
print(end - start)
