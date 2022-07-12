def swap(a,b):
    temp=a
    a=b
    b=temp

def next_permutation(arr):

    i=len(arr)-1
    if len(arr)==1:
        return arr
    if len(arr)==2:
        swap(arr[0],arr[1])
        return arr
    while i>0:






arr=[1,2,5,4,3,2]
next_permutation(arr)