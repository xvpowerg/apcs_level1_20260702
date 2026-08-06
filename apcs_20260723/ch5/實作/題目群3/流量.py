# 讀取 n, m, k
# n：伺服器數量
# m：城市數量
# k：方案數量
n, m, k = map(int, input().split())

# traffic[伺服器][城市]
# 代表某台伺服器要送多少流量到某個城市
traffic = []
for _ in range(n):
    traffic.append(list(map(int, input().split())))


# 算某一筆流量要花多少錢
def get_cost(amount, same_city):
    # 同城市：每單位 1 元
    if same_city:
        return amount

    # 不同城市：1000 以下，每單位 3 元
    if amount <= 1000:
        return amount * 3

    # 不同城市：超過 1000
    # 前 1000 單位，每單位 3 元
    # 超過的部分，每單位 2 元
    return 1000 * 3 + (amount - 1000) * 2


# best_cost：目前看過最便宜的方案
best_cost = 10**18
#注意相同城市出發 相同城市目的地才會相加
# 逐一檢查每一個方案
for _ in range(k):

    # plan[i] 代表伺服器 i 放在哪一個城市
    plan = list(map(int, input().split()))

    # city_flow[a][b]
    # 代表「城市 a 裡面的伺服器」總共要送多少流量到「城市 b」
    city_flow = []
    for _ in range(m):
        city_flow.append([0] * m)

    # 把每一台伺服器的流量，加到 city_flow 裡面
    for server in range(n):
        from_city = plan[server]

        for to_city in range(m):
            city_flow[from_city][to_city] += traffic[server][to_city]

    # 開始算這個方案的總費用
    total_cost = 0

    for from_city in range(m):
        for to_city in range(m):

            amount = city_flow[from_city][to_city]

            if from_city == to_city:
                total_cost += get_cost(amount, True)
            else:
                total_cost += get_cost(amount, False)

    # 更新最便宜答案
    if total_cost < best_cost:
        best_cost = total_cost

print(best_cost)