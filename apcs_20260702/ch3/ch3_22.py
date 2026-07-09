results = {"Ken":0,"Sean":0,"Lucy":0}

for i in range(5):
    vote = input("投票給: ")
    if vote not in results:
        print("無效票:",vote)
        continue
    results[vote] += 1

print(results)
