# Quick Sort
# for quickselect we assume all inputs are distinct 
import argparse
from random import randint,sample
def printArray(arr):
  print (' '.join(str(i) for i in arr))


def quicksort(arr, i, j):
  if i < j:
    pos = rand_partition(arr, i, j)
    quicksort(arr, i, pos - 1)
    quicksort(arr, pos + 1, j)

def rand_partition(A,s,e):
  i=randint(s,e)# both bounds are inclusive

  A[i],A[e]=A[e],A[i]
  return partition(A,s,e)

def partition(A, s, e):
  pivot = A[e]
  i = s - 1
  for j in range(s, e):
    if A[j] <= pivot:
      i += 1
      A[i],A[j]=A[j],A[i]

  A[e],A[i+1]=A[i+1],A[e]

  return i + 1
def select(A,s,e,k):
  if s==e:
    return A[s]
  p=rand_partition(A,s,e)
  i=p-s+1
  if k==i:
    return A[p]
  elif k<i:
    return select(A,s,p-1,k)
  else:
    return select(A,p+1,e,k-i)

#arr = [9, 4, 8, 3, 1, 2, 5]
#arr=[randint(0,30) for y in range(0,10)]
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--size",type=int,default=10)
  parser.add_argument("--min",type=int,default=0)
  parser.add_argument("--max",type=int,default=50)
  parser.add_argument("--algorithm",type=str,choices=["quicksort","quickselect"])
  args=parser.parse_args()
  n=args.size
  arr=sample(range(args.min,args.max),n)
  if args.algorithm == "quicksort":
    print(f"Initial array: {arr}")
    quicksort(arr,0,len(arr)-1)
    print(f"sorted array {arr}")
  else:
    k=randint(1,n)
    print (f"Initial Array sorted :{sorted(arr)}")
    print(f"{k}th smallest is {select(arr,0,len(arr)-1,k)}")





