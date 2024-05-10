#### there is something seriously wrong with the code   
### the counter is incremented when the case is accessed
### not when the item is used, as it should
## needs fixing
import numpy as np  
from numpy import random
C=4
values=np.array([3,1,2])
weights=np.array([1,2,2])
values=np.insert(values,0,0)
weights=np.insert(weights,0,0)
n=len(values)
counter=[0]*n
# can be "reused" 4 times
x=[2]*n
## add a dumpy value at the beginning of the arrays 


## initialise the solution matrix to 0
opt=[(C+1)*[0] for i in range(n)]

def F(i):
  global counter
  counter[i]+=1
  if counter[i]>=x[i]:
    return 1
 
  return 0

def knap_gen(values,weights,C):
  for j in range(1,C+1):
    counter=[0]*n
    for i in range(1,n):
    
      if j>=weights[i]:
        opt[i][j]=max(opt[i-1][j],values[i]+opt[i-F(i)][j-weights[i]])
        # opt1=values[i]+opt[i][j-weights[i]]
        # opt2=values[i]+opt[i-1][j-weights[i]]
        # opt3=opt[i-1][j]    
        # if counter[i]<x[i]:
        #   opt[i][j]=max(opt1,opt3)
        #   if opt[i][j]==opt1:
        #     counter[i]+=1
        # else:
        #   opt[i][j]=max(opt2,opt3)
      else:
        opt[i][j]=opt[i-1][j]

  return opt
def sol_gen(opt,weights,C):
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

opt=knap_gen(values,weights,C)
print(np.array(opt))
idx=sol_gen(opt,weights,C)
print(counter)
# print(values)
# print("solution idx:{}".format(idx))
# print("solution weights:{}".format(weights[idx]))
# print("solution values:{}".format(values[idx]))
# print(arrayToLatex(np.array(opt)))