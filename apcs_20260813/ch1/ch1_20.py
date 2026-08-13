import time,sys
input2 = sys.stdin.readline
print2 = sys.stdout.write
print2("輸入n:")
n = int(input2())
start = time.time()
out = []
for i in range(1,n+1):
    out.append(str(i*i))
print2(" ".join(out))
end = time.time()
print(f"time:{end - start:.4f}秒")
