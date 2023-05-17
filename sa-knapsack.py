import random
import math
import matplotlib.pyplot as plt
import numpy as np

# To try some random instances
# values=np.random.randint(1,50,200)
# weights=np.random.randint(1,50,200)
# KW=np.random.randint(50,250,1).item()


penalty=-100000
# This instance was solved using DP for comparison
# The optimal valueis 288
values=[48,13,17,4,27,46,47,37,22,36,49,4,43,44,32,13,17,6 ,45,26]
weights=[ 5, 32, 16, 49 , 8 ,17, 16, 22, 33, 40, 21, 17, 26, 34, 13,  5, 18, 44, 36, 14]
KW=100

# allocaed a list for the potential solution

current=[0]*len(values)

# it is better to create a feasible initial instance
# i.e. one where the sum of the weights is less than the weight of knapsack
def initial():
    total=0
    for i in range(len(values)):
        c=np.random.choice([0,1])
        if c==1:
            if total+weights[i]<=KW:
                current[i]=1
                total+=weights[i]
            else:
                break
    return current 

# Flip a single bit in the state
def neighbor(state):
    choice=random.randint(0,len(state)-1)
    #choice=np.random.randint(0,len(state)-1,1).item()
    next=state.copy()
    next[choice]=next[choice]^1
    return next
# the cost is just the sum of all values
# higher cost is desirable
def cost(state):
    w,v=0,0
    for i,s in enumerate(state):
        if s==1:
            w+=weights[i]
            v+=values[i]
    if w>KW:
        return penalty
    return v
max=0

# keep initial temperature low enough
# to prevent jumps to infeasible solution
temp=-penalty/50 # set it to, say, 0.1 to simulate local search 
alpha=0.9 #exp cooling rate. set it to 1 for local search
history=[0]
current=initial()
max_steps=10000
# main loop
for i in range(max_steps):
    
    next=neighbor(current)
    cc=cost(current)
    # append to history only if the state changed
    if cc!=history[-1]:
        history.append(cc)
    nc=cost(next)
    if cc>max:
        max=cc
        best=current[:]
    if nc>cc:
        current=next.copy()
    else:
        delta=cc-nc
        r=random.random()
        th=np.exp(-delta/temp)
        if r<th:
            current=next.copy()
    # not exactly exponential cooling
    # to prevent the temperature going to zero quickly
    if i%100==0:
        temp*=alpha
    

print(max,temp)
sol=[]
for i,x in enumerate(best):
    if x==1:
        sol.append(values[i])
sol.sort()
print(sol)
x=np.linspace(1,len(history),len(history))
plt.plot(x,history)
plt.show()