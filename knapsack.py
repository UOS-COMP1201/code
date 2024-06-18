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
#values=random.randint(1,50,10)
#weights=random.randint(1,50,10)
#C=random.randint(1,100)

# first element is a dummy element
#values=np.insert(values,0,0)
#weights=np.insert(weights,0,0)


#n=len(values)

# initialise the solution matrix to 0 


# 0-1 knapsack problem
def knap(values,weights,C):
  #v=np.insert(values,0,0)
  #w=np.insert(weights,0,0)
  v=[0]+values
  w=[0]+weights
  n=len(v)
  opt=[(C+1)*[0] for i in range(n)]
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=w[i]:
        opt[i][j]=max(opt[i-1][j],v[i]+opt[i-1][j-w[i]])
      else:
        opt[i][j]=opt[i-1][j]
  return opt
# knapsack problem with replacement, i.e. we can take the same item multiple times
def knap_repl(values,weights,C):
  #v=np.insert(values,0,0)
  #w=np.insert(weights,0,0)
  v=[0]+values
  w=[0]+weights
  n=len(v)
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=w[i]:
        u=opt[i-1][j]
        v=opt[i-1][j-w[i]]
        opt[i][j]=max(opt[i-1][j],v[i]+opt[i][j-w[i]])
      else:
        opt[i][j]=opt[i-1][j]

  return opt


# returns the actual solution for 0-1 knapsack
def sol(opt,weights,C):
  #w=np.insert(weights,0,0)
  w=[0]+weights
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=w[i]
    i-=1
  return [x-1 for x in sol]
# returns the actual solution for knapsack with replacement
def sol_repl(opt,weights,C):
  w=[0]+weights
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=w[i]
    else:
      i-=1
  return [x-1 for x in sol]

# examples
#opt=knap_repl(values,weights,C)
# opt=knap(values,weights,C)


weights=[20, 30, 40, 70]
values=[70, 80, 90, 200]
C=60
values=[5, 16, 9, 9, 5, 15, 20, 10, 6, 11]
weights= [8, 7, 6, 5, 6, 5, 9, 8, 6, 6]
C=19
opt=knap(values,weights,C)
#printLatex(opt)
#for i in range(n):
print("maximum value: {}".format(opt[-1][C]))
print("capacity:{}".format(C))
print("weights:{}".format(weights))
print("values:{}".format(values))
idx=sol(opt,weights,C)
print("solution weights:{}".format([weights[i] for i in idx]))
print("solution values:{}".format([values[i] for i in idx]))
print(f'indices (first item has index 0) {idx}')



