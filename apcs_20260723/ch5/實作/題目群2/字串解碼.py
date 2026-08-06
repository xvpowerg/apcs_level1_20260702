m, n = map(int, input().split())
es = [list(input()) for _ in range(m)]      #加密操作01字串集合
es.reverse()                                #操作字串集合反向
T = input()                                 #加密操作後字串
S = ""                                      #加密操作前字串
for e in es:                                #反向取出操作字串
    for i in range(-1, -len(e)-1, -1):      #反向取出0或1操作指令
        if e[i]=="1":                       #操作指令為1
            S = S + T[i]                    #T第i個字元接在S後面
        else:                               #操作指令為1
            S = T[i] + S                    #T第i個字元放在S前面
        #print(S)
    if e.count("1")%2==1:                   #操作字串有奇數個1
        mid = len(S)//2                     #字串中間點
        if len(S)%2==0:                     #偶數個字元
            S = S[mid:]+S[:mid]             #將字串S分成兩等份，前後順序交換
        else:                               #奇數個字元
            S = S[mid+1:]+S[mid]+S[:mid]    #中間的字元不動，前後順序交換
    #print(S)
    T, S = S, ""                            #字串還原
print(T)
