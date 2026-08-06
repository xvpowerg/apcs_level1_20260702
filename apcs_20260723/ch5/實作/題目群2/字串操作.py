def twoSwitch(s):       # 兩兩交換字元位置
    out = []
    for i in range(0, len(s), 2):
        out.append(s[i + 1])
        out.append(s[i])
    return ''.join(out)

def twoSort(s):         # 兩兩排序字元
    out = []
    for i in range(0, len(s), 2):
        f = s[i]
        s_char = s[i + 1]
        if f > s_char:
            f, s_char = s_char, f
        out.append(f)
        out.append(s_char)
    return ''.join(out)

def perfect(s):         # 完美重排：前半後半交錯組合
    h = len(s) // 2
    f = s[:h]
    t = s[h:]
    out = []
    for i in range(h):
        out.append(f[i])
        out.append(t[i])
    return ''.join(out)

s = input().strip()
k = int(input())
for _ in range(k):
    op = int(input())   # 讀取操作指令
    if op == 0:
        s = twoSwitch(s)
    elif op == 1:
        s = twoSort(s)
    elif op == 2:
        s = perfect(s)

print(s)    
