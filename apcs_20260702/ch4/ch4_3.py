def my_sum(a,b=0,c=0):
    ans = a + b + c
    return ans

print(my_sum(2,3))
print(my_sum(7))
print(my_sum(10,c=5,b=2))#具名參數 只要使用具名參數 之後都必須使用具名
