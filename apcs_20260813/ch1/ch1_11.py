def josphus(data,skip):
    idx = skip - 1
    while len(data) > 1:
        print(data,end="\t")
        print(data.pop(idx))
        idx = (idx + skip - 1)%len(data)
    print("surivor:",data[0])

n = int(input("輸入總人數"))
m = int(input("淘汰間距:"))
data = [i for i in range(1,n+1)]

josphus(data,m)
