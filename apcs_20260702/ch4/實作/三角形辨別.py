a,b,c = list(map(int, input().split()))
a,b,c = sorted([a,b,c]) #排序
print(a,b,c)

#驗證三角形
if a + b <= c:          #a+b<=c     ：無法構成三角形，印出 No
    print('No')
elif a**2+b**2<c**2:    #a*a+b*b<c*c：構成鈍角三角形，印出 Obtuse
    print('Obtuse')    
elif a**2+b**2==c**2:   #a*a+b*b=c*c：構成直角三角形，印出 Right
    print('Right')
else:                   #a*a+b*b>c*c：構成銳角三角形，印出 Acute
    print('Acute')
