def matrixAdd(A,B):
    n = len(A)
    m = len(A[0])
    C = [[0] * m for row in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

def printMatrix(arr):
    for data in arr:
        for v in data:
            print(v,end=" ")
        print()    
matrixA = [[1,3,5],
           [7,9,11],
           [13,15,17]]
matrixB = [[9,8,7],
           [6,5,4],
           [3,2,1]]
newArr = matrixAdd(matrixA,matrixB)
printMatrix(newArr)
