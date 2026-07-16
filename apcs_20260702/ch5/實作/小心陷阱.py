k = int(input())                    # 讀入初始值 k
x1, y1 = map(int, input().split())  # 讀入第一組條件 (x1, y1)
x2, y2 = map(int, input().split())  # 讀入第二組條件 (x2, y2)

i = 0                               # 位置 i 由 0 開始
while k > 0:                        # 當 k > 0 時持續進行迴圈
    i += k                          # 每次往前移動 k   
    if i % x1 == 0:                 # i 為 x1的倍數，k 減少 x2
        k -= y1
    if i % x2 == 0:                 # i 可以整除 x2，減少 k 值
        k -= y2

print(i)                            # 輸出最後停止時的位置 i
