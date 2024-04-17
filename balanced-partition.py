from numpy import *
import numpy as np  
num=5
x=random.randint(1,10,num)
x=[7,6,2,8,1]
sigma_half=int(sum(x)/2)

def bottom_up(x,num,sigma_half):
    opt=zeros((num+1,sigma_half+1),dtype=bool)    
    opt[:,0]=True
    for n in range(1,num+1):
        for s in range(1,sigma_half+1):
            if s-x[n-1]>=0:
                opt[n,s]=opt[n-1,s] or opt[n-1,s-x[n-1]]
            else:
                opt[n,s]=opt[n-1,s]

    return opt


    
def get_sol(opt,x,num,sigma_half):
    done=False
    n=num
    s=sigma_half
    sol=[]
    idx=[]
    while not (n==0 or s==0):
        if s-x[n-1]>=0 and opt[n-1,s-x[n-1]]==True:
            sol.append(x[n-1])
            s=s-x[n-1]
            idx.append(n-1)
        n=n-1
    # return the solution and the index of the selected elements
    return array(sol),array(idx)

def arrayToLatex(a):
    begin='\\begin{bmatrix}\n'
    end='\n\\end{bmatrix}\n'
    body=np.array2string(a,separator='&').replace('[','').replace(']','').replace(' ','').replace('\n','\\\\\n')
    return begin+body+end
opt=bottom_up(x,num,sigma_half)
print(sigma_half)
print(np.array2string(np.array(range(sigma_half+1)),separator=''))
print(opt.astype(int))
best=(where(opt[num]==True)[0])[-1]            
sol,idx=get_sol(opt,x,num,best)
print("x={}".format(x))
print("sol={} sum={}".format(sol,sum(sol)))
res=[]
for i,v in enumerate(x):
    if i not in idx:
      res.append(v)

print("res={} sum={}".format(res,sum(res)))  
print(arrayToLatex(opt.astype(int)))