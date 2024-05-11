'''
Dynamic programming solution to the knapsack problem
has two versions: one with replacement and one without
knap,sol functions are for the version without replacement
knap_repl,sol_repl functions are for the version with replacement
'''
import numpy as np  
from numpy import random
def printLatex(opt):
  n=len(opt)
  m=len(opt[0])
  for i in range(n):
    for j in range(m-1):
      print(f'{opt[i][j]}&',end='')
    print(f'{opt[i][m-1]}\\\\')
def arrayToLatex(a):
    begin='\\begin{bmatrix}\n'
    end='\n\\end{bmatrix}\n'
    body=np.array2string(a,separator='&').replace('[','').replace(']','').replace(' ','').replace('\n','\\\\\n')
    return begin+body+end
values=random.randint(1,50,10)
weights=random.randint(1,50,10)
C=random.randint(1,100)


weights=[20, 30, 40, 70]
values=[70, 80, 90, 200]
C=60

# first element is a dummy element
values=np.insert(values,0,0)
weights=np.insert(weights,0,0)


n=len(values)

# initialise the solution matrix to 0 
opt=[(C+1)*[0] for i in range(n)]

# 0-1 knapsack problem
def knap(values,weights,C):
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=weights[i]:
        opt[i][j]=max(opt[i-1][j],values[i]+opt[i-1][j-weights[i]])
      else:
        opt[i][j]=opt[i-1][j]
  return opt
# knapsack problem with replacement, i.e. we can take the same item multiple times
def knap_repl(values,weights,C):
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=weights[i]:
        u=opt[i-1][j]
        v=opt[i-1][j-weights[i]]
        opt[i][j]=max(opt[i-1][j],values[i]+opt[i][j-weights[i]])
      else:
        opt[i][j]=opt[i-1][j]

  return opt


# returns the actual solution for 0-1 knapsack
def sol(opt,weights,C):
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=weights[i]
    i-=1
  return sol
# returns the actual solution for knapsack with replacement
def sol_repl(opt,weights,C):
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=weights[i]
    else:
      i-=1
  return sol

# examples
#opt=knap_repl(values,weights,C)
# opt=knap(values,weights,C)
opt=knap(values,weights,C)
#printLatex(opt)
#for i in range(n):
print("maximum value: {}".format(opt[n-1][C]))
print("capacity:{}".format(C))
print("weights:{}".format(weights[1:]))
print("values:{}".format(values[1:]))
idx=sol(opt,weights,C)
print("solution weights:{}".format(weights[idx]))
print("solution values:{}".format(values[idx]))
print(f'indices {idx}')



