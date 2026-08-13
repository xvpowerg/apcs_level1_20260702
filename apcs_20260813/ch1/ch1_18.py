## 排序序列效能優化
import time
import bisect
import random
N = 100000
Q = 5000
data = sorted(random.sample(range(N*10),N))
queries = random.sample(range(N*10),Q)
print("data:",data[:101])
print("queries:",queries[:101])

lst = data.copy()
start = time.time()
for x in queries:
    lst.append(x)
    lst.sort()
sort_time = time.time() - start
print("append + sort time:",sort_time)

lst= data.copy()
start = time.time()
for x in queries:
    bisect.insort(lst,x)
bisect_time = time.time() - start
print("bisect_time:",bisect_time)


