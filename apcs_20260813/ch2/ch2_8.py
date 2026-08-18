arr = [2,3,1,2,4,3]
target = 7
n = len(arr)
l = 0
s = 0
ans = n + 1


for r in range(n):
    s += arr[r]    
    while s >= target:
        ans = min(ans,r-l+1)
        s -= arr[l]
        l+=1
print(ans if ans != n + 1 else 0)                
