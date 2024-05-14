import numpy as np
def max_subarray_sum(A):
   n=len(A)
   M=[0]*n
   M[0]=0
   m=0
   j=0
   last0=j
   for i in range(1,n):
        M[i]=max(0,M[i-1]+(A[i]-A[i-1]))
        if M[i]>m:
            m=M[i]
            j=last0
        if M[i]==0:
            last0=i
   return M,m,j
def msa(A):
   n=len(A)
   m=0
   j=0
   last0=j
   profit=0
   s=0
   for i in range(1,n):
       # M[i]=max(0,M[i-1]+(A[i]-A[i-1]))
        profit=max(0,profit+(A[i]-A[i-1]))
        if profit>m:
            m=profit
            j=last0
            s=i
        if profit==0:
            last0=i
   return m,j,s

# def msa(A):
#    n=len(A)
#    last=A[0]
#    m=A[0]
#    j=0
#    for i in range(1,n):
#         last=max(A[i],A[i]+last)
#         if last>m:
#             m=last
#             j=i
# #    max=A[0]
# #    for v in sums:
# #       if v>max:
# #          max=v

#    return m,j

# def get_subarray(M,A,j):
#     for i in range(j,-1,-1):
#         if M[i]==A[i]:
#             break
        
#     return A[i:j+1]
A=[-9,5,2,-4,6,3,-7,4,5,-5,-6,4,6,-4,3]
A=np.random.randint(1,20,10)
print(A)
#M,m,j=max_subarray_sum(A)
m,j,s=msa(A)

print(f'best profit={m},buy at {j},sell at {s}')
#print(get_subarray(M,A,j))