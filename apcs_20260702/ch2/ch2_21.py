AQI=201
if AQI >= 0 and AQI <= 50:
    print("良好")
elif 51 <=  AQI <= 100:
    print("普通")
elif AQI >= 101 and AQI <= 150:
    print("對敏感族群不健康")
elif 151  <=  AQI <= 200:
    print("對所有族群不健康")
else:
    print("非常不健康")
