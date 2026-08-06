N, M = map(int, input().split())    #讀取資料 N M ：群 個

LNums = []                          #將每筆資料中最大值，加入集合LNums
for i in range(N):                  #讀取N次，切割為M筆資料
    row = map(int, input().split())
    LNums.append(max(row))
#print(LNums)

S = sum(LNums)                      #LNums集合加總和為S

RNums = []                          #LNums集合中可將S整除的數字加入RNums集合
for l in LNums:
    if(S%l==0):
        RNums.append(l)

print(S)                            #輸出 S

if(len(RNums)!=0):                  #顯示最大值中可將S整除的數字
    print(*RNums)
else:                               #無資料顯示-1
    print(-1)
