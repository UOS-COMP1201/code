import numpy as np

#X="AAGCTTTGCCTT"
#Y="AAGCCTTTAGCC"
#X="BDC"
#Y="AABD"
#X="BDC"
#Y="ABDB"
#alpha_gap=0.5
#alpha=0.6
X="CG"
Y="CA"
alpha_gap=3
alpha=7

opt=np.zeros((len(X)+1,len(Y)+1))
for i in range(0,len(X)+1):
    opt[i,0]=i*alpha_gap
for i in range(0,len(Y)+1):
    opt[0,i]=i*alpha_gap
    
for i in range(1,len(X)+1):
  for j in range(1,len(Y)+1):
    if X[i-1]==Y[j-1]:
        cost=0
    else:
        cost=alpha
    opt[i,j]=min(cost+opt[i-1,j-1],alpha_gap+opt[i,j-1],alpha_gap+opt[i-1,j])
 
i=len(X)
j=len(Y)
solX=[]
solY=[]
while i!=0 and j!=0:
    if X[i-1]==Y[j-1]:
        cost=0
    else:
        cost=alpha
    if opt[i,j]==cost+opt[i-1,j-1]:
        solX.insert(0,X[i-1])
        solY.insert(0,Y[j-1])
        i=i-1
        j=j-1
    elif opt[i,j]==alpha_gap+opt[i,j-1]:
        solX.insert(0,"-")
        solY.insert(0,Y[j-1])
        j=j-1
    else:
        i=i-1
        solX.insert(0,X[i-1])
        solY.insert(0,"-")

MX="".join(solX)
MY="".join(solY)
print(opt)
print(MX)
print(MY)
