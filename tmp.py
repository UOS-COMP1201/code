import numpy as np
from numpy import random
x=list(random.randint(1,20,10))
y=list(random.randint(1,20,10))
d=[[0 for _ in range(len(x))] for _ in range(len(y))]
for i,a in enumerate(x):
  for j,b in enumerate(y):
    d[i][j]=abs(a-b)
print(np.array(d))
z=y.copy()
print(x)
print(y)
x.sort(reverse=True)
y.sort()
total=0
for i,v in enumerate(x):
  total+=abs(v-y[i])

print(total)
total=0
for i,v in enumerate(x):
  total+=abs(v-z[i])
print(total)