subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]
dataList = list(zip(subjs,scores))#打包
print(dataList)
for v1,v2 in dataList:
    print(v1,v2)
