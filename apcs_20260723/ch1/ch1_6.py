def c1(a,b):
    ans = a + b
    return ans

def c2(a,b):
    ans = a * b
    return ans

def c3(a,b):
    ans = a - b
    return ans
action = int(input("計算動作 1 加法 2 乘法 3 減法"))

if action == 1:
    myFunc = c1
elif action == 2:
    myFunc = c2
elif action == 3:
    myFunc = c3
    
print(myFunc(2,5))
