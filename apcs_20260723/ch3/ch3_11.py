from collections import deque
q = deque([55,66,77,88,99])
q.append(6)
print(q)
q.appendleft(8)
print(q)
q.rotate(2)#往右推
print(q)
q.rotate(-3)#往左推
print(q)
f = q.popleft()#彈出第一筆
print(f)
print(q)
f = q.pop()#彈出最後一筆
print(f)
print(q)
