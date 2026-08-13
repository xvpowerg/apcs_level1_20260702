import time
start = time.time()

for i in range(1,5):
    for j in range(1,5):
        if i ==j:
            continue
        for k in range(1,5):
            if k == i or k ==j:
                continue
            for x in range(1,5):
                if x ==i or x ==j or x ==k:
                    continue
                print(f"{i}{j}{k}{x}")
                
print("time:",time.time() - start)
