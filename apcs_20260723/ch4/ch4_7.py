def fib_rec(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2 ##上上次相加的數字
        num2 = nextNum#上次相加的數字
        nextNum = num1 + num2
    return   nextNum  
#i = 2
# num1 = 1
# num2 = 1
# nextNum = num1 + num2 2
# i = 3
# num1 = 1
# num2 = 2
# nextNum = num1 + num2 3

print("fib_rec:",fib_rec(10))
print("fib_it:",fib_it(10))
