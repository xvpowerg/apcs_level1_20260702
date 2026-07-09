count = 1
answer = 5
guess = int(input("猜一個數字"))

while True:
    if guess == answer:
        break
    count += 1
    guess = int(input("再猜一次"))
print("猜了幾次:",count)    
print("完成")    


