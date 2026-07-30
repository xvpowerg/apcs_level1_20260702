scores = [[50,60,70,0,0],
          [30,40,50,0,0],
          [70,80,90,0,0],
          [66,77,88,0,0],
          [22,33,44,0,0]]
for i in range(len(scores)):
    sSum = 0
    for j in range(3):
        sSum += scores[i][j]
        if scores[i][j] < 60:
            scores[i][4] += 1
    scores[i][3] = sSum / 3        

subjs = [[0] * 3 for _ in range(2)]#2x3陣列
for x in range(3):
    subjSum = 0
    for y in range(5):
        subjSum += scores[y][x]
        if scores[y][x] < 60:
            subjs[1][x] += 1#不及格人數
            
    subjs[0][x] = subjSum / 5
print("座號\t國文\t英文\t數學\t平均\t不及格")
for i in range(len(scores)):
    print(i+1,end="\t")
    for j in range(5):
        print(scores[i][j],end="\t")
    print()
print("平均",end="\t")
for x in range(3):
    print(f"{subjs[0][x]:.1f}",end="\t")
print()
print("不及格",end="\t")
for x in range(3):
    print(f"{subjs[1][x]}",end="\t")
print()    
#print(subjs)
