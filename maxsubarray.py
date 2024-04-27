def max_subarray_sum(A):
   n=len(A)
   M=[0]*n
   M[0]=A[0]
   m=A[0]
   j=0
   for i in range(1,n):
        M[i]=max(A[i],A[i]+M[i-1])
        if M[i]>m:
            m=M[i]
            j=i
   return M,m,j

def msa(A):
   n=len(A)
   last=A[0]
   m=A[0]
   j=0
   for i in range(1,n):
        last=max(A[i],A[i]+last)
        if last>m:
            m=last
            j=i
#    max=A[0]
#    for v in sums:
#       if v>max:
#          max=v

   return m,j

def get_subarray(M,A,j):
    for i in range(j,-1,-1):
        if M[i]==A[i]:
            break
        
    return A[i:j+1]
A=[-9,5,2,-4,6,3,-7,4,5,-5,-6,4,6,-4,3]
print(A)
M,m,j=max_subarray_sum(A)
print(get_subarray(M,A,j))