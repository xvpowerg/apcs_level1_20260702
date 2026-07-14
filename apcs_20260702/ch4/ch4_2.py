def c2f(c):
    f = 9 / 5 * c + 32
    return f

while True:
    inStr = input("請輸入攝氏溫度(輸入q離開)")
    if inStr == 'q':
        print("程式結束")
        break
    tc = float(inStr)
    ans = c2f(tc)
    print(f"攝氏{tc:.2f}度等於華氏{ans:.2f}度")
