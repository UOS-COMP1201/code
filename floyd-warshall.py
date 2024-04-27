import numpy as np
# DP solution for the all-pairs shortest path problem using the Floyd-Warshall algorithm
# adjacency matrix representation, with edge weights, for the example in the notes
# added a row and column at index 0 to make the indexing easier
# so now the "real" nodes are 1,2,3,4 instead of 0,1,2,3
adjm=np.array([ [0, float('inf'), float('inf'),float('inf'),float('inf')],
                [float('inf'),0, float('inf'), 3, float('inf')],
                [float('inf'),2, 0, float('inf'),float('inf')],
                [float('inf'),float('inf'), 7, 0, 1],
                [float('inf'),6, float('inf'), float('inf'), 0]])
n=4 # excluding the extra node
d=np.empty((n+1,n+1,n+1))
d[0]=adjm
# remember range(1,n+1) goes from 1 to n
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
                d[k,i,j]=min(d[k-1,i,j],d[k-1,i,k]+d[k-1,k,j])
for i in range(n+1):
    print(f'iteration {i}') 
    print(d[i,1:,1:])
