scores = [87,66,90,65,70]
score_sum = 0
count = len(scores)
score_max = 0
score_min = 100
for i in range(count):
    print(f"第{i+1}學生的成績:{scores[i]}")
    score_sum += scores[i]
    if scores[i] > score_max:
        score_max = scores[i]
    if scores[i] <  score_min:
        score_min = scores[i]
print("總分:",score_sum)
print("最高分:",score_max)
print("最低分:",score_min)        
