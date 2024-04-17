import numpy as np
num=5
items=np.random.randint(1,20,num+1)
items=[0,2,8,3,13,7]
#items=[0,2,3,4,8,10]
#x=array([12,8,6,13,7])
value=np.random.randint(20,30,1).item()
value=12
#value=7


def bottom_up(x,num,value):
    opt=np.zeros((num+1,value+1),dtype=bool)    
    opt[:,0]=True
    for n in range(1,num+1):
        for s in range(1,value+1):
            if s-x[n]>=0:
                opt[n,s]=opt[n-1,s] or opt[n-1,s-x[n]]
            else:
                opt[n,s]=opt[n-1,s]

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
r=subset_sum(items,num,value)
opt=bottom_up(items,num,value)
solution=None
print(items[1:],value)
print(arrayToLatex(opt.astype(int)))
print(r)
if r==True:
    solution=get_sol(opt,items,num,value)
    print(solution)
    
            
            
