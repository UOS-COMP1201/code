# this is a dynamic programming solution to the rod cutting problem
# as given in leetcode problem 1547 solved in tutorial 9 NOT the one in the lecture
import numpy as np
from functools import cache 
import math
# length of rod and cuts
n=7
cuts=[4]
n=26875
cuts=[17059,24270,10139,22853,1817,8494,4374,5762,20148,522,20381,14428,1829,25688,24934,9930,756,15959,20596,14322,17368,7821,14432,21840,4757,25249,16394,9087,23958,8453,14889,5120,2324,5513,4431,22619,19200,17302,3976,21893,13725,25766,11266,9370,19889,7382,21249,13925,24908,14255,17761,10991,21983,10561,24670,9891,25014,18629,5201,15323,25051,23409,11458,4861,12334,25865,19886,1487,24174]
print(sorted(cuts))

def minCost(n, cuts):

    opt=np.empty((n+1,n+1),dtype=int)
    opt.fill(-1)
    cuts=[0]+cuts+[n]
    cuts.sort()
    ## i couldn't figure out why the following code is not working
    # sometimes it gives the correct answer and sometimes it doesn't
    @cache
    def dp(a, b):
            
                if a == b:
                    return 0
                m=100000
                parts=[x for x in cuts if x>a and x<b ]
                if parts==[]:
                    return 0
                for k in parts:
                    m=min(m,dp(a,k) + dp(k, b))
                return m+b-a
    ## memoization is slower than using @cache
    def dfm(i, j):
            # i and j are the indices of the cuts array
            # not positions !
            if opt[i][j]!=-1:
                return opt[i][j]
            if i+1==j:
                  return 0
            
            minCost=math.inf
            for k in range(i+1,j ):
                 minCost=min(minCost,dfm(i,k) + dfm(k,j))
            opt[i][j]=minCost+cuts[j]-cuts[i]
            #return minCost+cuts[j]-cuts[i]
            return opt[i][j]  
    @cache      
    def dfs(i, j):
            # i and j are the indices of the cuts array
            # not positions !
            if i+1==j:
                  return 0
            
            minCost=math.inf
            for k in range(i+1,j ):
                 minCost=min(minCost,dfs(i,k) + dfs(k,j))
            return minCost+cuts[j]-cuts[i]
    def bu(cuts):
        n=len(cuts)
        opt=np.zeros((n,n),dtype=int)
        #opt=np.empty((n,n))
        #opt=[[0]*n for i in range(n)]
        for length in range(2,n):
            for i in range(n-length):        
                j=i+length
                opt[i,j]=math.inf
                for k in range(i+1,j):
                    opt[i,j]=min(opt[i,j],opt[i,k]+opt[k,j])
                #opt[i][j]=min([opt[i][k]+opt[k][j] for k in range(i+1,j)])
                opt[i,j]+=cuts[j]-cuts[i]
        return opt[0,n-1]
    #return dp(0, n)    
    return dfm(0, len(cuts)-1) 
    #return dfs(0, len(cuts)-1) 
    #return bu(cuts)
print(minCost(n,cuts) )

