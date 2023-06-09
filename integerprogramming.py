# -*- coding: utf-8 -*-
"""integerprogramming.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/UOS-COMP1201/code/blob/main/integerprogramming.ipynb

<a href="https://colab.research.google.com/github/UOS-COMP1201/code/blob/main/integerprogramming.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

c=np.array([4,5])
A=np.array([[1,4],[3,-4]])
#b=np.array([10,6])
#b=np.array([90,60])
#b=np.array([80,70])     
b=np.array([101,70])
x1_bounds=(0,None)
x2_bounds=(0,None)

import copy
max=0

def IP(c,A,b,bounds,depth):
  global max
  res=linprog(c,A,b,bounds=bounds)
  if res.fun == None:
    print("pruned by infeasibility depth {}".format(depth))
    return 
  if -res.fun<max:
    print(-res.fun,res.x)
    print("pruned by bound depth {}".format(depth))
    return 
  result=-res.fun
  # at this point result>max
  print(result,res.x)
  int_sol=True
  for var in res.x:
    if np.floor(var)!=np.ceil(var):
      int_sol=False
      break
  if  int_sol:
        max=result
        return
  # not all variables are integers, branch      
  for i,var in enumerate(res.x):
    fl=np.floor(var)
    cl=np.ceil(var)
    
    if fl!=cl:
      print("branching on {} {} depth {}".format(fl,cl,depth))
      tmp=copy.deepcopy(bounds)
      tmp[i]=(cl,tmp[i][1])
      IP(c,A,b,tmp,depth+1)
      tmp=copy.deepcopy(bounds)
      tmp[i]=(tmp[i][0],fl)
      IP(c,A,b,tmp,depth+1)
   

  return res.fun,res.x

c=[-x for x in c]
r=IP(c,A,b,[x1_bounds,x2_bounds],0)

