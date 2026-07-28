def dev_to_bin2(num):
    myList = []
    while True:
        num,reminder = divmod(num,2)
        myList.append(str(reminder))
        if num == 0:
            return "".join(myList[::-1])
def dec_to_hex(num):
    base = ["0","1","2","3","4","5","6","7","8","9",
            "A","B","C","D","E","F"]
    myList = []
    while True:
        num,reminder = divmod(num,16)
        myList.append(base[reminder])
        if num == 0:
            return "".join(myList[::-1])
x = 45        
print(dev_to_bin2(x))
print(dec_to_hex(x))

