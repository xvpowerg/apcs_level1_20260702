x = [5,15,25,35,45]
for v in x:
    print(v,end=" ")
print()
for i in range(len(x)):
    print(x[i],end=" ")
print()
x.insert(2,100)
print(x)
x.append(200)
print(x)
x[2] = 20
print(x)
x.remove(20)
print(x)
y = x.pop()
print("pop:",y)
print(x)
z = x.pop(2)
print("pop:",z)
print(x)
