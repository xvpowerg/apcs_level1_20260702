N = int(input())                        # 有幾個人
BF = list(map(int, input().split()))    # BF[i] 代表：第 i 個人的最好朋友是誰

visited = [False] * N                   # visited[i] 代表第 i 個人有沒有被算過
ans = 0                                 # ans 用來數有幾個小群體

for i in range(N):                      # 從第 0 個人看到第 N-1 個人
    if visited[i]:                      # 如果這個人已經算過了
        continue                        # 就跳過，不用再算一次

    ans += 1                            # 發現一個新的小群體

    x = i                               # 從這個人開始走
    while not visited[x]:               # 只要這個人還沒算過
        visited[x] = True               # 就把他標記成「算過」
        x = BF[x]                       # 走到他的最好朋友那裡

print(ans)                              # 印出小群體的數量