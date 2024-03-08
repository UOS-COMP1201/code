from numpy import *
num=5
items=random.randint(1,20,num+1)
items=[0,12,8,6,13,7]
#items=[0,2,3,4,8,10]
#x=array([12,8,6,13,7])
value=random.randint(20,30,1).item()
value=26
#value=7


def bottom_up(x,num,value):
    opt=zeros((num+1,value+1),dtype=bool)    
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
    while not (n==0 or s==0):
        if s-x[n]>=0 and opt[n,s-x[n]]==True:
            sol.append(x[n])
            s=s-x[n]
        n=n-1
    return array(sol)

r=subset_sum(items,num,value)
opt=bottom_up(items,num,value)
solution=None
print(items[1:])
print(value)
print(r)
if r==True:
    solution=get_sol(opt,items,num,value)
    print(solution)
    
            
            
