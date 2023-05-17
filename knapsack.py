import numpy as np


#values=np.random.randint(1,50,20)
#weights=np.random.randint(1,50,20)
#w=np.random.randint(50,150,1).item()

values=[48,13,17,4,27,46,47,37,22,36,49,4,43,44,32,13,17,6 ,45,26]
weights=[ 5, 32, 16, 49 , 8 ,17, 16, 22, 33, 40, 21, 17, 26, 34, 13,  5, 18, 44, 36, 14]
w=100

n=len(values)
opt=[(w+1)*[0] for i in range(n+1)]

# base cases
for i in range(n+1):
  opt[i][0]=0
for j in range(w+1):
  opt[i][0]=0

# DP optimal value
def getOpt():

  for i in range(1,n+1):
    for j in range(1,w+1):
      idx=i-1
      if j>=weights[idx]:
        u=opt[i-1][j]
        v=opt[i-1][j-weights[idx]]
        opt[i][j]=max(opt[i-1][j],values[idx]+opt[i-1][j-weights[idx]])
      else:
        opt[i][j]=opt[i-1][j]
  return opt

# walk backwards to obtain the actual solution
def getSol(opt):
  global n,w
  sol=[]
  while w>0 and n>0:
    if opt[n][w]>opt[n-1][w]:
      sol.append(values[n-1])
      w-=weights[n-1]
    n-=1
  return sol

opt=getOpt()
# print the optimal table
for i in range(n+1):
  print(opt[i])

sol=getSol(opt)
sol.sort()
print(sol)

