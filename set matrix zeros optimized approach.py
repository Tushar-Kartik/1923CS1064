def setmatrixzeros(matrix,n,m):

    rowzero=False
    for i in range(0,n):
        for j in range(0,m):
            if matrix[i][j]==0:
                matrix[0][j]=0
                if i>0:
                    matrix[i][0]=0
                else:
                    rowzero=True


    for i in range(1,n):
        for j in range(1,m):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j]=0
    if matrix[0][0]==0:
        for i in range(n):
            matrix[i][0]=0
    if rowzero== True:
        for j in range(m):
            matrix[0][j]=0

    return matrix

matrix=[[1,0,1],[1,1,1],[1,1,1]]
n=len(matrix)
m=len(matrix[0])
print(setmatrixzeros(matrix,n,m))





