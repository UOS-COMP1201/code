from random import randint
import argparse
# radomized select including the case
# when non-distinct elements are present
def partition(A,s,e):
    i=s-1
    k=s
    j=e
    pivot=A[e]
    while k<j :
        if A[k]>pivot:
            k+=1
        elif A[k]<pivot:
            i+=1
            A[i],A[k]=A[k],A[i]
            k+=1
        else:
            j-=1
            A[j],A[k]=A[k],A[j]
    return i,j
def select(A,s,e,k):
    if s>=e:
        return A[s]
    m=randint(s,e)
    pivot=A[m]
    A[m],A[e]=A[e],A[m]
    i,j=partition(A,s,e)
    if k<=i-s+1:
        return select(A,s,i,k)
    elif k<=i-j+e-s+2:
        return pivot
    else:
        return select(A,i+1,j-1,k-(i-j+e-s+2))


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size",type=int,default=10)
    parser.add_argument("--k",type=int,default=5)
    parser.add_argument("--min",type=int,default=0)
    parser.add_argument("--max",type=int,default=50)
    args=parser.parse_args()
    A=[randint(args.min,args.max) for x in range(args.size)]
    a=A.copy()
    a.sort()
    print(f"sorted array a={a}")
    k=args.k
    m=select(A,0,len(A)-1,k)
    print(f"the {k} the smallest element is {m}")
