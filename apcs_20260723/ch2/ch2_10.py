myList = [i for i in range(1,11)]
print(myList)
myList2 = [i**2 for i in range(1,11)]
print(myList2)
dic1 = {x:x**3 for x in range(1,11)}
print(dic1)

myList3  = [x for x in range(1,11) if x % 2 == 0]
print(myList3)
