'''
Dynamic programming solution to the knapsack problem
has two versions: one with replacement and one without
knap,sol functions are for the version without replacement
knap_repl,sol_repl functions are for the version with replacement
'''
def printLatex(opt):
  n=len(opt)
  m=len(opt[0])
  for i in range(n):
    for j in range(m-1):
      print(f'{opt[i][j]}&',end='')
    print(f'{opt[i][m-1]}\\\\')
#values=random.randint(1,50,20)
#weights=random.randint(1,50,20)
# first element is a dummy element
##weights=[0,1,3,5,7,8]
##values=[0,3,4,5,6,7]
weights=[0,2,3,4,5]
values=[0,2,3,4,6]

C=13
n=len(values)
opt=[(C+1)*[0] for i in range(n)]
for i in range(n):
  opt[i][0]=0
for j in range(C+1):
  opt[i][0]=0
def knap(values,weights,C):
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=weights[i]:
        u=opt[i-1][j]
        v=opt[i-1][j-weights[i]]
        opt[i][j]=max(opt[i-1][j],values[i]+opt[i-1][j-weights[i]])
      else:
        opt[i][j]=opt[i-1][j]
  return opt

def knap_repl(values,weights,C):
  for i in range(1,n):
    for j in range(1,C+1):
      if j>=weights[i]:
        u=opt[i-1][j]
        v=opt[i-1][j-weights[i]]
        opt[i][j]=max(opt[i-1][j],values[i]+opt[i][j-weights[i]])
      else:
        opt[i][j]=opt[i-1][j]

  return opt


def sol(opt,weights,C):
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=weights[i]
    i-=1
  return sol
def sol_repl(opt,weights,C):
  n=len(opt)
  i=n-1
  j=C
  sol=[]
  while i>0 and j>0:
    if opt[i][j]!=opt[i-1][j]:  
      sol.insert(0,i)
      j-=weights[i]
    else:
      i-=1
  return sol

#opt=knap_repl(values,weights,C)
opt=knap(values,weights,C)
printLatex(opt)
for i in range(n):
  print(opt[i])
# print(sol_repl(opt,weights,C))
print(sol(opt,weights,C))