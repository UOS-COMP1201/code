import numpy as np  
n=16
v=np.random.randint(1,20,n)
# comment out the above line and uncomment the following line
# to use the same array as in the lecture

#v=np.array( [1,6,8,7,2,3,15,4] )

# insert a dummy element at the beginning of the array
# so that the index of the elements starts  from 1
v=np.insert(v,0,0)
n=len(v)-1
#https://gist.github.com/hikmatfarhat-ndu/f6501ff1f08691c31327ecd5ba5d3422
opt=np.zeros((n+1))
# in Python range(1,n+1) goes from 1 to n

for i in range(1,n+1):
    opt[i]=max(opt[i-1],v[i]+opt[i-2])
def recover_solution(opt,v):
    i=len(v)-1
    sol=[]
    while i>0:
        if opt[i]==opt[i-1]:
            i-=1
        else:
            sol.append(v[i])
            i-=2
    return sol
print(opt)
print(recover_solution(opt,v))  