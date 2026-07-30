def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()    
def matrixMutiply(A,B):
    m = len(A)#row 2
    na = len(A[0])#colum 3
    nb = len(B) #row 3
    p = len(B[0])#colum 2
    if na != nb:
        print("無法相乘")
        return
    C = [[None]*p  for _ in range(m)]
    for i in range(m):
        for j in range(p):
            tmp = 0
            for k in range(nb):
                tmp += A[i][k] * B[k][j]
            C[i][j] = tmp
    return C        
matrixA = [[6,3,5], [8,9,7]]
matrixB = [[5,10], [14,7], [6,8]]
matrix = matrixMutiply(matrixA,matrixB)
printMatrix(matrix)
