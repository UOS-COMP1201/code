"""
this is my answer
"""
def min_cost_trip(cost):
    
    n = len(cost)
    min_cost = [float('inf')] * n
    min_cost[0] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and min_cost[i] + cost[i][j] < min_cost[j]:
                    min_cost[j] = min_cost[i] + cost[i][j]

    return min_cost

# Example usage
# # n = int(input("Enter the number of stations: "))
# # cost = []

# # print("Enter the cost matrix row by row:")
# # for i in range(n):
# #     row = list(map(int, input().split()))
# #     cost.append(row)
cost = [
    [0, 4, 6, 1],
    [4, 0, 4, 6],
    [6, 4, 0, 1],
    [1, 6, 1, 0]
]
minimal_cost = min_cost_trip(cost)
print(f"The minimal cost is {minimal_cost}.")
## claude suggests the code below
## when prompted that it does not give the right
## answer it apologises and gives the "corrected"
## algorithms the SAME while claiming that it 
## gives the correct answer !
def min_cost_trip(n, c):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + c[j][i])

    return dp[2]  # Return cost to reach station 3

n = 4
c = [
    [0, 4, 6, 1],
    [4, 0, 4, 6],
    [6, 4, 0, 1],
    [1, 6, 1, 0]
]

result = min_cost_trip(n, c)
print(f"Minimum cost from station 1 to station 3: {result}")

## chatgpt
def find_min_cost(c):
    n = len(c)
    # Initialize min_cost array with infinity
    min_cost = [float('inf')] * n
    min_cost[0] = 0  # Cost to reach station 1 from itself is 0
    
    # Iterate through all stations
    for j in range(1, n-1):
        for i in range(n):
            if min_cost[i] + c[i][j] < min_cost[j]:
                min_cost[j] = min_cost[i] + c[i][j]
    
    return min_cost[n-2]  # Return the cost to reach station n-1

# Example usage:
cost_matrix = [
    [0, 4, 6, 1],
    [4, 0, 4, 6],
    [6, 4, 0, 1],
    [1, 6, 1, 0]
]

min_cost = find_min_cost(cost_matrix)
print(f"The minimum cost to reach station n-1 is: {min_cost}")
