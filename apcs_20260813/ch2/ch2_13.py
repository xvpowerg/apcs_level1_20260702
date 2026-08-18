from math import fabs
def sqrt_binary(x,pre=2):
    x1,x2 = 0,x
    y = (x1 + x2)/2
    while fabs(y*y - x) > 10 ** (-pre):
        if y*y > x:
            x2 = y
        else:
            x1 = y
        y = (x1 + x2) / 2
    return y
num = int(input("輸入整數"))
print(f"{num}的平方根{sqrt_binary(num):.3f}")
