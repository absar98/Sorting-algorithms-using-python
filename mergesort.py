import math
def merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    
    l=list(range(n1+1))
    R=list(range(n2+1))
    
    for i in range(0,n1):
        l[i]=A[p+i-1]
    for j in range(0,n2):
        R[j]=A[q+j]
    l[i+1],R[j+1] = math.inf,math.inf
    i,j = 0,0
    for k in range(p-1,r,1):
        if l[i]<=R[j]:
            A[k]=l[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
def mergesort(A,p,r):
    if p<r:
        q=int(math.floor((p+r-1)/2))
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
        return A
    A=[12,233,232,423,2,1,1,221,22]
    p=mergesort(A,0,len(A))
    print(p)
    