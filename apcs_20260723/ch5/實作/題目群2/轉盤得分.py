def rotate(l, r):           # 轉盤旋轉
    r %= n                  # 每列長度為n,將右轉位數r在0~n-1
    return l[-r:] + l[:-r]  # 右轉：將最後 r 個放前面，前面 n-r 個接在後面

def score(l2):              # 計分
    counts = {}             # 建立字典，統計每個字元的出現次數
    for c in l2:
        counts[c] = counts.get(c,0)+1   # 字元出現次數+1, 未出現過為0
    return max(counts.values())         # 回傳出現最多次的字元的次數

m, n, k = map(int, input().split())     
arrs = [list(input()) for _ in range(m)]
ops = [[int(x) for x in input().split()] for _ in range(k)]

total=0                          # 用來累加總得分
for i in range(k):               # 執行每一輪的轉動操作
    for j in range(m):
        arrs[j]=rotate(arrs[j],ops[i][j])   # 把第j列依據 ops[i][j]進行旋轉
    #print(arrs)
    for a in range(n):
        #print([row[a] for row in arrs]) # 第a欄：arrs[0][a], arrs[1][a],., arrs[m-1][a]
        total+=score([row[a] for row in arrs]) # 計分
print(total)
