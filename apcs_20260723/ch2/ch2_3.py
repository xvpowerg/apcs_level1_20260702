a1 = int(input("輸入首項"))
d = int(input("輸入公差:"))
n = int(input("輸入項數"))

for i in range(n):
    print(a1 + i * d,end=" ")

print()
def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) + d

for i in range(1,n+1):
    print(getAn(i),end=" ")
