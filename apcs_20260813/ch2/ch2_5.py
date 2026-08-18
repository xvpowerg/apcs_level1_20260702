import time

def fib_dp(n,memo=None):
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    elif n == 1 or n==2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_dp(n-2,memo) + fib_dp(n-1,memo)
    return memo[n]
start = time.time()
fib_dp(37)
end = time.time()
print(end - start)
