n = int(input())

roles = []                                      # 先準備一個空串列
for _ in range(n):                              # 重複讀取 n 個角色
    role = list(map(int, input().split()))      # 讀取一位角色：[攻擊力, 防禦力]
    roles.append(role)                          # 把這位角色放進 roles

#print(roles)

for i in range(n):
    ability = roles[i][0]**2 + roles[i][1]**2   # 計算能力值
    roles[i].insert(0, ability)                 # 插入索引0，變成[能力,攻擊,防禦]

roles.sort(reverse=True)                        # 先看索引0，依能力值由大到小排序
#print(roles)

print(roles[1][1], roles[1][2])                 # 輸出第二名的攻擊力與防禦力