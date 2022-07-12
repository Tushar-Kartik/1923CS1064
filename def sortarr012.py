def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def sortarrayof012(arr):
    l=0
    r=len(arr)-1
    i=0

    def swap(a,b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    while i<=r:
        if arr[i]==0:
            swap(i,l)
            l+=1
        elif arr[i]==2:
            swap(i,r)
            r-=1
            i-=1  #we dont want to increament when swapping with r
        i+=1

    return arr

arr=[2,2,1,1,1,2,0,0,0]
print(sortarrayof012(arr))
