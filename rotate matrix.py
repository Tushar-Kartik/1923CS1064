def rotate_matrix(matrix):

    l=0
    r=len(matrix) - 1

    while l<r:
        for i in range ( r - l):
            top , bottom = l , r
            temp = matrix[top][l+i]

            #to move bottom left to top left
            matrix[top][l+i]=matrix[bottom - i][l]

            #to move bottom right to bottom left
            matrix[bottom - i][l]=matrix[bottom][r - i]

            #matirx top right into bottom right
            matrix[bottom][r - i]=matrix[top + i][r]

            # temp to matrix top right
            matrix[top + i][r]=temp
        l += 1
        r -= 1
    return matrix
matrix=[[5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]]
print(rotate_matrix(matrix))