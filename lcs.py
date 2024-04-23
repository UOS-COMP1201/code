import numpy as np

def lcs(x,y):

    n=len(x)
    m=len(y)
    M=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                M[i][j]=1+M[i-1][j-1]
            else:
                M[i][j]=max(M[i-1][j],M[i][j-1])
    return M

x="ABCD"
y="AABDC"
M=lcs(x,y)
print(np.array(M))