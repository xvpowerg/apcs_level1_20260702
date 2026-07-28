'''
撰寫一個程式，檢查使用者輸入的數值
1 是否為遞增
2 是否為正負交錯
'''
num = int(input("輸入陣列數量"))
arr = [0] * num
for i in range(num):
    arr[i] = int(input(f"輸入第{i+1}筆數值"))
for j in range(num-1):
    if arr[j] >=arr[j+1]:
        print("不是遞增")
        break
else:
    print("是遞增")
