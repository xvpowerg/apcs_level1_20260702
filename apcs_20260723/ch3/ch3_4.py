def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j],end=" ")
        print()    
def flip(matrixA):
    matrixB = []
    r = len(matrixA)
    for i in range(r-1,-1,-1):
        matrixB.append(matrixA[i])
    return matrixB

