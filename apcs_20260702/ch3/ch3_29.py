def get_sum(a,b):
    ans = a + b
    #print(ans)
    return ans #回傳ans
def get_pow(a,n):
    ans = a ** n
    print(ans)

x = 2
y = 3
v = get_sum(x,y)
print(v)#None 表示空 什麼都沒有
get_pow(v,2)

x1 = 5
y1 = 3
get_pow(get_sum(x1,y1),2)

