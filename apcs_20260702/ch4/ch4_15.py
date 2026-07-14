myList = [7,1,9,5,3]
#預設小到大
newList =  sorted(myList)
print("myList:",myList)
print(newList)

myList.sort()
print("myList:",myList)
myList.sort(reverse=True)
print("myList reverse:",myList)#大到小

