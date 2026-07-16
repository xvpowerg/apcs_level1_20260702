a,b,c=map(int,input().split())      #取值並轉型
a,b,c=sorted([a,b,c], reverse=True) #反向排序
if a==b and b==c:                   #三數相等
    print("3",a)
elif (a!=b and b==c):               #a不同b,c相等
    print("2",a,b)
elif (a==b and b!=c):               #a,b相等c不同
    print("2",b,c)    
else:                               #三數不相等
    print("1",a,b,c)
