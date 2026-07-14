def myMap(data):
    result = []
    for v in data:
        result.append(int(v))#字串轉換整數
    return  result

myData = ["88","77","66"]
print(myData)
dataList = myMap(myData)
print(dataList)
print(sum(dataList))


