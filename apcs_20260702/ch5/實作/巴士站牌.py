n = int(input())  # 讀取站牌數量
minD, maxD = 10000, 0  # 儲存最短距離、最長距離用的變數
xp, yp = map(int, input().split())  # 讀取第1支站牌的位置

for _ in range(1, n):
    xc, yc = map(int, input().split())  # 依序讀取第2到n支站牌的位置
    dis = abs(xc - xp) + abs(yc - yp)  # 計算這支站牌與前一支站牌的距離
    minD = min(minD, dis)  # 更新最短距離
    maxD = max(maxD, dis)  # 更新最長距離
    xp, yp = xc, yc  # 更新前一支站牌的位置

print(f"{maxD} {minD}")  # 印出答案    
