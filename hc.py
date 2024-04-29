adj={}
adj['a']=['b','c','d']
adj['b']=['a','c','f']
adj['c']=['a','b','d','e']
adj['d']=['a','c','e']
adj['e']=['c','d','f']
adj['f']=['b','e']

def HC(source,u,path,n):
    for v in adj[u]:
        if v==source and n==1:
            return True
        if v not in path:
            path.append(v)
            r=HC(source,v,path,n-1)
            if r:
                return True
            else:
                path.pop(-1)
    return False
source='a'
path=[source]
r=HC(source,source,path,len(adj))
if r:
    print("Hamiltonian Cycle exists")
    print(path+[source])
else:
    print("Hamiltonian Cycle does not exist")
