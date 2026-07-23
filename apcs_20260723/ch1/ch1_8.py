list1 = [1,2,3,4,5]
def myPow(x):
    return x ** 2
pwFun = myPow
list2 = list(map(pwFun,list1))
print(list2)
