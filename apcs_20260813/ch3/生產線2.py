n, m = map(int, input().split())        #取得機器數n及工作數m
d = [0]*(n+2)                           #差分數列
for _ in range(m):
    l, r, w = map(int, input().split()) #l-r的機器工作量為w
    d[l] += w                           #左端點l位置+w
    d[r+1] -= w                         #右端點r下一個位置-w
#print(d)
loads = [0]*(n+2)                       #各機器工作負載
for i in range(1, n+1):
    loads[i] = loads[i-1]+d[i]          #差分序列作前綴和
loads.pop(0)                            #取出前後加入的0
loads.pop()                             
#print(loads)
t = [int(x) for x in input().split()]   #機器工作時間
loads.sort(reverse=True)                #依機器工作量由大到小排列
t.sort()                                #機器工作時間由小到大排列                             
#print(loads)
total = 0                               #工作總時間             
for i in range(n):
    total += loads[i]*t[i]
print(total)
