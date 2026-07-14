#讀取輸入數值字串 X
numStr = input()
 
#取得奇數位數值和 A 及取得偶數位數值和 B
A, B = 0, 0
numLen = len(numStr)
for i in range(-1, -numLen-1, -1):
    if(i%2!=0): 
        A = A + int(numStr[i])
    else:       
        B = B + int(numStr[i])
 
# 計算秘密差並列印
x = abs(A-B)
print(x)