### this solution is provided by Claude 3

def optimal_schedule(tasks):
    # Sort tasks by deadline
    tasks.sort(key=lambda x: x[1])
    
    n = len(tasks)
    max_deadline = max(task[1] for task in tasks)
    
    # Initialize dp table
    dp = [[0] * (max_deadline + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(max_deadline + 1):
            # If we don't include this task
            dp[i][j] = dp[i-1][j]
            
            # If we include this task
            duration, deadline, profit = tasks[i-1]
            if j >= duration and j <= deadline:
                dp[i][j] = max(dp[i][j], dp[i-1][j-duration] + profit)
    
    # Find the maximum profit
    max_profit = max(dp[n])
    
    # Backtrack to find the schedule
    schedule = []
    j = dp[n].index(max_profit)
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            schedule.append(i-1)
            j -= tasks[i-1][0]
    
    schedule.reverse()
    
    return max_profit, schedule

# # Example usage
# tasks = [
#     (2, 4, 10),  # (duration, deadline, profit)
#     (1, 2, 5),
#     (2, 3, 15),
#     (3, 5, 20)
# ]

# max_profit, optimal_schedule = optimal_schedule(tasks)

# print(f"Maximum profit: {max_profit}")
# print("Optimal schedule (task indices):", optimal_schedule)
# print("Tasks to be executed:")
# for i in optimal_schedule:
#     print(f"Task {i+1}: Duration = {tasks[i][0]}, Deadline = {tasks[i][1]}, Profit = {tasks[i][2]}")



## this is my solution
tasks=[('A',3,8,100),('B',2,6,59),('C',1,9,40),
       ('D',2,5,70),('E',4,10,101),('F',5,10,140)]
c_tasks=[task[1:] for task in tasks]
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
  #print(tasks)
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
print("claude")

max_profit, optimal_schedule = optimal_schedule(c_tasks)
print(optimal_schedule)