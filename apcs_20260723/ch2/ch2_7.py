arr1 = [[5,6,7],[8,11,19]]#2x3
print(arr1[0])
print(arr1[1])
print(arr1[0][1])

for arr in arr1:
    for v in arr:
        print(v,end=" ")
    print()    

print("===================")

rowLen = len(arr1)
for i in range(rowLen):
    colLen = len(arr1[i])
    for c in range(colLen):
        print(f"({i},{c})",arr1[i][c])
    print()        
