'''
撰寫一個程式，檢查使用者輸入的數值
1 是否為遞增
2 是否為正負交錯
'''
num = int(input("輸入陣列數量"))
arr = [0] * num
for i in range(num):
    arr[i] = int(input(f"輸入第{i+1}筆數值"))
    
for k in range(num-1):
    if arr[k]*arr[k+1] >=0:
        print("不是正負交錯")
        break
else:
    print("是正負交錯")
print(arr)    

