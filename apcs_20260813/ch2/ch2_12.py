def find_max(arr,left,right):
    if left == right:
        return arr[left]
    mid = (left+right)//2
    max_left = find_max(arr,left,mid)#左半邊
    max_right = find_max(arr,mid +1 ,right)#右半邊
    return max(max_left,max_right)

import random
data = random.sample(range(1,100),16)
print(data)
result = find_max(data,0,len(data) - 1)
print("最大值:",result)
