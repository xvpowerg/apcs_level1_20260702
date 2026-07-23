def myMap(myList,func):
    result = []
    for i in myList:
        result.append(func(i))
    return result

myData = [2,6,8,9,11]
myDataStr = myMap(myData,str)
v1 = "-".join(myDataStr)
print(v1)

myData2 = ["10","9","2"]
ans = sum(myMap(myData2,int))
print(ans)
