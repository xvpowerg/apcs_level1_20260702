def myMap(f,data):
    result = []
    for v in data:
        result.append(f(v))#字串轉換整數
    return  result

myData = ["88","77","66"]
print(myData)
dataList = myMap(int,myData)#字串轉整數
print(dataList)

myData2 = [88,77,66]
dataList2 = myMap(str,myData2)#整數轉字串
print(dataList2)
