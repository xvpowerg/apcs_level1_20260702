#前綴和

arr = [2,3,5,7,11]
n = len(arr)
ps = [0] * (n + 1)
for i in range(1,n+1):
    ps[i] = ps[i-1] + arr[i-1]
print(ps)

#1~3總和
print(sum(arr[1:4]))

print(ps[4] - ps[1])



