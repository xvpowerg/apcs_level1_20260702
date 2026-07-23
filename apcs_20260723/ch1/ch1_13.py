myList2 = [(8,2),(1,7),(3,5),(4,1)]
myList2.sort()
print(myList2)
#key 指定使用List內容的甚麼排序
myList2.sort(key=lambda x:x[1],reverse=True)
print(myList2)
