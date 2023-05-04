tasks=[('A',3,8,100),('B',2,6,59),('C',1,9,40),
       ('D',2,5,70),('E',4,10,101),('F',5,10,140)]
# sort by deadline
tasks=sorted(tasks,key=lambda x:x[2])
for t in tasks:
  print(t)
#exit()
w=tasks[-1][2]
print(w)
# initialization
n=len(tasks)
opt=[ [0 for j in range(w+1)] for i in range(n+1)]
print(opt)
#opt=[(w+1)*[0] for i in range(n+1)]
# for j in range(w+1):
#   opt[0][j]=0

# main loops
for i in range(1,n+1):
  for t in range(0,w+1):
    tp=min(tasks[i-1][2],t)-tasks[i-1][1]# can task finish by deadline
    if tp>=0:#yes
      u=opt[i-1][t]
      v=tasks[i-1][3]+opt[i-1][tp]
      opt[i][t]=max(u,v)
    else:#no
      opt[i][t]=opt[i-1][t]
# print the solution matrix. The value in the last row, last column is the optimal value
for i in range(n+1):
  print(opt[i])
def getJobs(sol,tasks):
  i=len(opt)-1 # rows
  j=len(opt[0])-1 # columns
  task_list=[]
  print(tasks)
  while i>0 and j>0:
    task=tasks[i-1]
    if sol[i][j]==sol[i-1][j]: # not included
      i-=1
    else:
      task_list.append(task)
      j=min(j,task[2])-task[1]
      i-=1
  return task_list


task_list=getJobs(opt,tasks)
print(task_list)