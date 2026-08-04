def gcd_it(m,n):
    while n != 0:
        #m 被除數
        #n 除數
        r = m % n
        m = n #除數變被除數
        n = r #餘數變除數
    return m


print(gcd_it(20,14))
