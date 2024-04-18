def max_subarray_sum(A):
   n=len(A)
   M=[0]*n
   M[0]=A[0]
   m=A[0]
   for i in range(1,n):
        M[i]=max(A[i],A[i]+M[i-1])
        if M[i]>m:
            m=M[i]
#    max=A[0]
#    for v in sums:
#       if v>max:
#          max=v

   return m

def msa(A):
   n=len(A)
   last=A[0]
   m=A[0]
   for i in range(1,n):
        last=max(A[i],A[i]+last)
        if last>m:
            m=last
#    max=A[0]
#    for v in sums:
#       if v>max:
#          max=v

   return m


A=[2,-4,6,3,-7,4,5,-5,-6,4,6,-4,3]
print(msa(A))