import time

start = time.time()
total = 0
for x in range(1,10000):
    total += x
print(f"1+....+10000 = {total}")
end = time.time()
print(f"自行運算時間:{end - start:.4f}秒")

start = time.time()
total = sum(range(1,10000))
print(f"sum:{total}")
end = time.time()
print(f"sum()耗時:{end - start:.4f}秒")


