def compareM(m1,m2):                #定義比對矩陣距離函式
    cnt=0                           #兩矩陣距離:對應位置元素不相同的數量
    global r                        #全域變數r,距離門檻
    for i in range(len(m1)):        
        for j in range(len(m1[0])):
            if m1[i][j]!=m2[i][j]:  #對應位置值不相同,cnt+1
                cnt += 1    
    #print(m1, m2, cnt)
    return cnt<=r                   #傳回距離是否小於門檻

s,t,n,m,r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(s)]
b = [list(map(int, input().split())) for _ in range(n)]
suma = sum(sum(r) for r in a)       #矩陣a數值總和
count=0                             #符合條件的子矩陣個數
mDiff=float('inf')                  #子矩陣與矩陣a總和相差最小值,預設無窮大
for i in range(n-s+1):              #逐一取b的子矩陣
    for j in range(m-t+1):
        b1 = [row[j:j+t] for row in b[i:i+s]]   #b的子矩陣
        if compareM(a, b1):                     #比對矩陣距離函式是否低於門檻
            count+=1                            #符合次數+1
            sumb = sum(sum(r) for r in b1)      #子矩陣總和
            mDiff = min(mDiff,abs(sumb-suma))   #更新矩陣相差最小值

print(count)                            #符合條件的子矩陣個數
print(mDiff if count!=0 else -1)        #矩陣相差最小值,沒有符合條件的子矩陣輸出-1
