import numpy as np
# adjacency list representation, with edge weights, for the example in the notes
# a->b, w=-1, a->c, w=3 is represented as [(1,-1),(2,3)]
#a=0,b=1,c=2,d=3,e=4,f=5
adj=[[(1,-1),(2,3)],[(3,6)],[(1,-5),(4,2),(5,4)],[(1,-3)],[(5,-7)],[(3,-1)]]
# comment out the above line and uncomment the line below to test the negative cycle detection
# we create a negative cycle by changing the weight from edge b->d from 6 to -6
#adj=[[(1,-1),(2,3)],[(3,-6)],[(1,-5),(4,2),(5,4)],[(1,-3)],[(5,-7)],[(3,-1)]]


# compute the reversed adj list
def reverse_adj(adj):
    n=len(adj)
    radj=[[] for _ in range(n)]
    for i in range(n):
        for j,w in adj[i]:
            radj[j].append((i,w))
    return radj
radj=reverse_adj(adj)
#print(radj)
# compute the shortest path from a (node 0) to all other nodes
def bellman_ford(radj):
    n=len(radj)
    # initialise the distance matrix to infinity
    d=np.array([[float('inf') for _ in range(n)] for _ in range(n+1)])
    # distance from the source to itself is 0 for all iterations
    d[:,0]=0
    # iterating n-1 times is enough to find the shortest path in a graph with no negative cycles
    # here we are iterating one more time to detect negative cycles
    # Note that in Python range(1,n+1) goes from 1 to n
    for iter in range(1,n+1):
        # iterate over all nodes
        for u in range(0,n):
            d[iter,u]=d[iter-1,u]
            for v,cost in radj[u]:
                if d[iter-1,v]+cost<d[iter,u]:
                    d[iter,u]=d[iter-1,v]+cost
    return d
d=bellman_ford(radj)
# check for negative cycles
for i in range(len(radj)):
    # d[last iteration] < d[second to last iteration] means that there is a negative cycle
    if d[-1,i]<d[-2,i]:
        print('Negative cycle detected')
        break
# print the distance matrix
# here we take the transpose so the output is similar to the example in the notes
print(d.T)