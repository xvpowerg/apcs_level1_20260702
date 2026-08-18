#差分
A = [3,8,5,11,7,14]
n = len(A)
D = [0] * (n+1)
D[0] = A[0]

for i in range(1,n):
    D[i] = A[i] - A[i - 1]
print("原本A:",A)
print("原本D:",D)

left = 1
right = 4
x = 2
D[left] += x
D[right+1] -= x
print("跟X算完的D:",D)

new_A=[0]*n
new_A[0] = D[0]
for i in range(1,n):
    new_A[i] = new_A[i-1] + D[i]
print("更新 A:",new_A)    



