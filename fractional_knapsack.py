import queue
from numpy import *


values=random.randint(1,50,20)
weights=random.randint(1,50,20)
w=asscalar(random.randint(1,100,1))
p=queue.PriorityQueue()
for i,v in enumerate(values):
    p.put((weights[i]/v,i))
sol=[]
ow=w

while w>0:
    x=p.get()
    if weights[x[1]]<w:
      sol.append((x[1],1))
      w=w-weights[x[1]]
    else:
        
      f=w/weights[x[1]]
      sol.append((x[1],f))  
      w=0
