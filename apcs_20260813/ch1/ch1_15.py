import time

N = 200000

data_list = list(range(N))
data_set = set(data_list)

target = N - 1
repeat = 5000
# 測試 set in
start = time.time()
for _ in range(repeat):
    if target in data_set:
        pass
set_time = time.time() - start
print("set in time:",set_time)

#測試list in
start = time.time()
for _ in range(repeat):
    if target in data_list:
        pass
list_time = time.time() - start
print("list in time:",list_time)
