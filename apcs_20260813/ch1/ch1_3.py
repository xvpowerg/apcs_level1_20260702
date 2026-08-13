#print(chr(65))#數字轉字母#
#print(ord('A'))#字母轉數字
c = 65
for i in range(0,5):
    for j in range(0,5):
        if j ==i:
            continue
        for k in range(0,5):
            if k == j or k == i:
                continue
            for x in range(0,5):
                if x ==i or x == j or x == k:
                    continue
                for m in range(0,5):
                    if m == i or m ==j or m == k or m == x:
                        continue
                    print(f"{chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+x)},{chr(c+m)}")
                
