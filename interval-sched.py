import numpy as np
# insert a dummy element at the beginning of the array
# so that the index of the elements starts  from 1
# The values below correspond to the intervals in the lecture
# (starting time, ending time, weight)
intervals=[(0,0,0),(1,3,2),(2,6,3),(3,7,2),(7,9,2),(6,10,6)]
# sort by finishing time
intervals.sort(key=lambda x:x[1])
# Compute the predecessor p of each interval using binary search
# for a total of O(n log n)
def compute_p(intervals):
    def binary_search(intervals,i):
        low=1
        high=i-1
        while low<=high:
            mid=(low+high)//2
            if intervals[mid][1]<=intervals[i][0]:
                if intervals[mid+1][1]<=intervals[i][0]:
                    low=mid+1
                else:
                    return mid
            else:
                high=mid-1
        return 0
    p=[]
    p.append(0)
    for i in range(1,len(intervals)):
        p.append(binary_search(intervals,i))
    
    return p
def compute_opt(intervals):
    n=len(intervals)-1
    opt=np.zeros((len(intervals)))
    p=compute_p(intervals)
    for i in range(1,n+1):
        opt[i]=max(intervals[i][2]+opt[p[i]],opt[i-1])
    return opt
def recover_solution(intervals,opt,p):
    i=len(intervals)-1
    sol=[]
    while i>0:
        if opt[i]>opt[i-1]:
            sol.append(intervals[i])
            i=p[i]
        else:
            i-=1
    return sol   
# example
p=compute_p(intervals)
opt=compute_opt(intervals)
print(opt)

print(recover_solution(intervals,opt,p))