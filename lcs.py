# Dynamic Programming solution to the longest common subsequence problem
# numpy used to have a nice output when  printing the matrix. Not used otherwise 
import numpy as np


def lcs(x,y):

    n=len(x)
    m=len(y)
    # initialise solution matrix to 0
    M=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                M[i][j]=1+M[i-1][j-1]
            else:
                M[i][j]=max(M[i-1][j],M[i][j-1])
    return M
# return the actual subsequence 
def get_seq(x,y,M):
    i=len(x)
    j=len(y)
    seq=[]
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            # we are adding symbols in reverse order
            seq.append(x[i-1])
            i-=1
            j-=1
        elif M[i-1][j]>M[i][j-1]:
            i-=1
        else:
            j-=1
        # return the reversed sequence
    return seq[::-1]

x="ABCD"
y="AABDC"
M=lcs(x,y)
print(np.array(M))
print(get_seq(x,y,M))