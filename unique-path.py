n=6
m=6
opt=[[0]*m for i in range(n)]
for i in range(m):
    opt[0][i]=1
for i in range(n):
    opt[i][0]=1
for i in range(1,n):
    for j in range(1,m):
        opt[i][j]=opt[i-1][j]+opt[i][j-1]
print(opt[n-1][m-1])
