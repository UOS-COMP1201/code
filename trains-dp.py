"""
this is the answer of ChatGPTs
"""
def min_cost_trip(cost):
    """
    Calculate the minimal cost of a trip from station 1 to station n.

    Args:
    cost (list of list of int): A 2D list where cost[i][j] is the cost of traveling directly from station i to station j.

    Returns:
    int: The minimal cost to travel from station 1 to station n.
    """
    n = len(cost)
    min_cost = [float('inf')] * n
    min_cost[0] = 0

    for i in range(n):
        for j in range(i + 1, n):
            if min_cost[i] + cost[i][j] < min_cost[j]:
                min_cost[j] = min_cost[i] + cost[i][j]

    return min_cost[-1]

# Example usage
n = int(input("Enter the number of stations: "))
cost = []

print("Enter the cost matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    cost.append(row)

minimal_cost = min_cost_trip(cost)
print(f"The minimal cost to travel from station 1 to station {n} is {minimal_cost}.")
