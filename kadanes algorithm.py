def maxsumsubarray(arr):

    maxsub=arr[0]
    currsum=0
    for n in arr:

        if currsum<0:
            currsum=0
        currsum = currsum + n
        maxsub=max(maxsub,currsum)
    return maxsub

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxsumsubarray(arr))
