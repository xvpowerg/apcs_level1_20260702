#可給函式參數預設值
def get_sum(a,b,c=0):
    return a + b + c
ans = get_sum(2,5)
print(ans)
ans = get_sum(2,5,3)
print(ans)
