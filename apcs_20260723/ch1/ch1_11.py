actionList = [lambda x : x+2, lambda x:x **2,lambda x:x * 8]
myData = [3,4,5]
for v in myData:
    for func in actionList:
        print(func(v), end=" ")
    print()    



