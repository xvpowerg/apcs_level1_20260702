import time,sys

n = int(input("輸入 n:"))
start = time.time()
for i in range(1,n+1):
    print(i*i,end=" ")
end = time.time()
print(f"標準輸入出耗時:{end - start :.4f}秒")
