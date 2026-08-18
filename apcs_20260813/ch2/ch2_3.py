import time
arr = list(range(1,10000))
def solve1():
    start = time.time()
    global arr
    total = 0
    for x in arr:
        total += x
    print(total)
    end = time.time()
    print(f"使用全域變數耗時{end - start}秒")

def solve2():
    start = time.time()
    local_arr = arr
    total = 0
    for x in local_arr:
        total += x
    print(total)
    end = time.time()
    print(f"使用區域變數耗時{end - start}秒")
    
solve1()
solve2()
