n = int(input())
w1,w2,h1,h2=map(int, input().split())
vs = list(map(int,input().split()))
a1=w1*w1        # 下層底面積
a2=w2*w2        # 上層底面積
v1=a1*h1        # 下層(剩餘)容量
v2=a2*h2        # 上層(剩餘)容量

maxh=0          # 最大上升高度

for v in vs:            # 逐一取出加水量
    if v<=v1:           # 加水後下層仍有空間
        h = v//a1       # 本次上升高度
        v1-=v           # 下層剩餘容量減少,上層剩餘容量不變
    elif v1<v<=v1+v2:           # 加水後下層已滿,上層仍有空間
        h = v1//a1+(v-v1)//a2   # 本次上升高度
        v1=0                    # 下層已滿
        v2-=(v-v1)              # 上層剩餘容量減少
    else:                   # 加水後容器已滿
        h = v1//a1+v2//a2   # 本次上升高度
        v1,v2=0,0           # 上下層都滿
        maxh = max(h,maxh)  # 挑戰先前最大上升高度
        break               # 提前終止
    maxh = max(h,maxh)      # 挑戰先前最大上升高度    
print(maxh) # 列印最大上升高度
