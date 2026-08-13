import time
from collections import deque

N = 100000

lst = []

start = time.time()
for i in range(N):
    lst.append(i)
list_append_time = time.time() - start
print("list append tail:",list_append_time)

dq = deque()

start = time.time()

for i in range(N):
    dq.append(i)
deque_append_time = time.time() - start
print("deque_append(taill):",deque_append_time)
