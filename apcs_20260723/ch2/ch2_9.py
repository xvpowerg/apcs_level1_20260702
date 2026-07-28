myList = []
count = 1
for i in range(2):
    dataList = []
    for k in range(1,11):
        dataList.append(count)
        count += 1
    myList.append(dataList)    
print(myList)
