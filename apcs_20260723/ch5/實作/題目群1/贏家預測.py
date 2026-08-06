n, m = map(int, input().split())
S = [-1]+[int(s) for s in input().split()]  #索引可以直接取得戰力
T = [-1]+[int(t) for t in input().split()]  #索引可以直接取得應變力
idx = [int(i) for i in input().split()]     #當前玩家編號
lCnt = [-1]+[0]*n                           #索引取得失敗次數
while len(idx)>1:                           #只剩一個玩家時結束
   # print(1, idx, S, T, lCnt)
    wins, loses = [], []                    #本輪勝利組與失敗組
    for i in range(0,len(idx),2):
        p1 = idx[i]                         #玩家一編號
        if i==len(idx)-1:                   #玩家一落單
            wins.append(p1)                 #直接晉級下一輪,數值不變
            break
        p2 = idx[i+1]                       #玩家二編號
        a,b,c,d = S[p1],T[p1],S[p2],T[p2]   #玩家戰力應變力數值
        if a*b>=c*d:                        #玩家一勝
            S[p1]=a+c*d//(2*b)
            T[p1]=b+c*d//(2*a)
            S[p2]=c+c//2
            T[p2]=d+d//2
            w, l = p1, p2
        else:                               #玩家二勝
            S[p2]=c+a*b//(2*d)
            T[p2]=d+a*b//(2*c)
            S[p1]=a+a//2
            T[p1]=b+b//2
            w, l = p2, p1
        lCnt[l]+=1                          #失敗者失敗次數+1
        wins.append(w)                      #獲勝者加入勝利組
        if lCnt[l]<m:                       #失敗者仍未淘汰
            loses.append(l)                 #失敗者加入失敗組
    idx = wins+loses                        #下一輪順序:勝利組+未淘汰失敗組
   # print(2,idx, S, T, lCnt, end='\n\n')
print(idx[0])  
