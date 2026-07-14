import random
ans = random.randint(1,5)#隨機產生1~5的數字
guess = int(input("輸入數字"))
if guess == ans:
    print("正確")
else:
    print("失敗")
