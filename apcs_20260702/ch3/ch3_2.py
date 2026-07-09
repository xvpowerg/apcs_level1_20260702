h = float(input("輸入身高"))
w = int(input("輸入體重"))
bmi = w / ((h / 100)**2)
print("bmi:",bmi)

if bmi > 30:
    print("肥胖")
elif bmi > 25:
    print("過重")
elif bmi > 18.5:
    print("正常")
elif bmi > 0:
    print("過輕")
else:
    print("數值錯誤")

