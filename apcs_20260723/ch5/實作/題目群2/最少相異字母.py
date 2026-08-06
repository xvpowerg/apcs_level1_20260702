def compareRule(s):                     #自訂排序方法
    return len(set(s)), s               #先比較不重複字元長度
                                        #長度相同字典排序比較
n = int(input())                        #取得字串數量
strs = [input() for _ in range(n)]      #取得字串集合
strs1 = sorted(strs, key=compareRule)   #以自訂排序方法
print(strs1[0])                         #排序最小者為最和諧字串
