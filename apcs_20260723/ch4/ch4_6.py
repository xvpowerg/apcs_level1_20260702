#m 被除數
#n 除數
def gcd_rec(m,n):
    if n == 0:
        return m
    else:
        return gcd_rec(n,m%n)
#除數變被除數
#餘數變除數
print(gcd_rec(20,14))    
