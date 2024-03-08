#import queue
#from numpy import *
def printLatex(opt):
  n=len(opt)
  m=len(opt[0])
  for i in range(n):
    for j in range(m-1):
      print(f'{opt[i][j]}&',end='')
    print(f'{opt[i][m-1]}\\\\')
#values=random.randint(1,50,20)
#weights=random.randint(1,50,20)
# first element is a dummy element
weights=[0,1,3,5,7,8]
values=[0,3,4,5,6,7]
#w=asscalar(random.randint(1,100,1))
w=9
n=len(values)
opt=[(w+1)*[0] for i in range(n)]
for i in range(n):
  opt[i][0]=0
for j in range(w+1):
  opt[i][0]=0
for i in range(1,n):
  for j in range(1,w+1):
    if j>=weights[i]:
      u=opt[i-1][j]
      v=opt[i-1][j-weights[i]]
      opt[i][j]=max(opt[i-1][j],values[i]+opt[i-1][j-weights[i]])
    else:
      opt[i][j]=opt[i-1][j]
printLatex(opt)
for i in range(n):
  print(opt[i])
def sol(opt,weights,w):
  n=len(opt)
  m=len(opt[0])
  i=n-1
  #j=m-1
  j=w
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=weights[i]
    i-=1
  return sol

print(sol(opt,weights,w))