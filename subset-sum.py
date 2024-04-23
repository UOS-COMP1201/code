import numpy as np
num=5
items=np.random.randint(1,20,num+1)
items=[0,2,8,3,13,7]
#items=[0,2,3,4,8,10]
#x=array([12,8,6,13,7])
value=np.random.randint(20,30,1).item()
value=12
#value=7

def as_knapsack(weights,C):
    n=len(weights)-1
    opt=np.zeros((n+1,C+1),dtype=int)
    # no matter how many items we have, if the target is 0 (C=0)
    # we have a solution since the empty set is a subset of any set
    opt[:,0]=1
    # no matter what the target is (other than 0), if we have no items, we can't have a solution
    opt[0,1:]=0
    for i in range(1,n+1):
        for s in range(1,C+1):
            if s-weights[i]>=0:
                opt[i,s]=max(opt[i-1,s],opt[i-1,s-weights[i]])
            else:
                opt[i,s]=opt[i-1,s]
    return opt

def bottom_up(x,value):
    # -1 because we inserted a zero at the beginning
    n=len(x)-1   
    opt=np.zeros((n+1,value+1),dtype=bool)
    opt[:,0]=True
    for i in range(1,n+1):
        for s in range(1,value+1):
            if s-x[i]>=0:
                opt[i,s]=opt[i-1,s] or opt[i-1,s-x[i]]
            else:
                opt[i,s]=opt[i-1,s]

    return opt

def subset_sum(A,n,s):
    if s==0:
        return True
    if n==0:
        return False
    if s-A[n]>=0:
        return subset_sum(A,n-1,s) or subset_sum(A,n-1,s-A[n])
    else:
        return subset_sum(A,n-1,s)
    
def get_sol(opt,x,num,value):
    n=num
    s=value
    sol=[]
    # this function is called only if the solution exists
    # this means opt[n,s] is True as a starting point
    while not (n==0 or s==0):
        if s-x[n]>=0 and opt[n-1,s-x[n]]==True:
            sol.append(x[n])
            s=s-x[n]
        n=n-1
    return np.array(sol)

def arrayToLatex(a):
    begin='\\begin{bmatrix}\n'
    end='\n\\end{bmatrix}\n'
    body=np.array2string(a,separator='&').replace('[','').replace(']','').replace(' ','').replace('\n','\\\\\n')
    return begin+body+end
# r=subset_sum(items,num,value)
# opt=bottom_up(items,value)
# solution=None
# print(items[1:],value)
# print(arrayToLatex(opt.astype(int)))
# print(r)
# if r==True:
#     solution=get_sol(opt,items,num,value)
#     print(solution)
opt=as_knapsack(items,value) 
print(opt)
            
            
