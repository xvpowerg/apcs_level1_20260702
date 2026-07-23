list1 = [1,2,3,4,5]

pwFun = lambda x : x**2 #他就是一個函式只是換個語法
list2 = list(map(pwFun,list1))
print(list2)
