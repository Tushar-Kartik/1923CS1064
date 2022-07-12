def generate(n):

    res=[[1]]
    for i in range(n-1): #n-1 coz we have already created one
        temp=[0]+res[-1]+[0]
        row=[]
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    return res

n=5
print(generate(n))