import time
from collections import deque

N = 100000
lst = []

start = time.time()

for i in range(N):
    lst.insert(0,i)
list_insert_front_time = time.time() - start
print("list_insert_front_time:",list_insert_front_time)

dq = deque()

start = time.time()

for i in range(N):
    dq.appendleft(i)
deque_appendleft_time = time.time() - start
print("deque_appendleft_time:",deque_appendleft_time)
