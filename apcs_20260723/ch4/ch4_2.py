cars = ["Audi", "Honda", "Mazda", "Ford", "Benz", "Lexus", "BMW"]
print(cars)
car = input("輸入車廠名稱:")
for i in range(len(cars)):
    if car == cars[i]:
        print(f"位置是:{i}")
        break
else:
    print("不存在")
