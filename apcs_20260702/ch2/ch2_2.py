h = float(input('身高單位公分'))
w = int(input("請輸入體重公斤"))
bmi = w / ((h / 100) ** 2)
print("bmi:",bmi)
print("bmi:",round(bmi,2))#取到小數點第二位

