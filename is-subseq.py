x="acb"
y="ahbgdc"

def isSubsequence(s, t):
    
    def aux(x, y,i,j):
        if len(x)> len(y):
            return False
        if i==len(x):
            return True
        for k in range(j,len(y)):
            if x[i] == y[k]:
                return aux(x,y,i+1,k+1)
        return False
    return aux(s,t,0,0)

def aux(s,t):
    j=len(t)-1
    i=len(s)-1
    f=True
    for i in range(len(s)-1,-1,-1):
        f= False

        for k in range(j,-1,-1):
            if s[i]==t[k]:
                j=k-1
                f=True
                break
        if not f:
            break
    return f
#print(isSubsequence(x,y))
print(aux(x,y))