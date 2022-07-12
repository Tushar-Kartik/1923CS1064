def setmatirxzeros(matrix,n,m):
    row=[1]*n
    col=[1]*m

    for i in range(0,n):
        for j in range(0,m):
            if matrix[i][j]==0:
                row[i] = 0
                col[j] = 0

    for i in range(0,n):
        for j in range(0,m):
            if row[i]==0:
                matrix[i][j]=0
    for j in range(0,m):
        for i in range(0,n):
            if col[j]==0:
                matrix[i][j]=0


    return matrix

matrix=[[1,1],[1,1],[1,1]]
numrows=len(matrix)
numcols=len(matrix[0])
print(numrows,numcols)

res=setmatirxzeros(matrix,numrows,numcols)
print(res)