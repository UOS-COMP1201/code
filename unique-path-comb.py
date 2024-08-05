"""
question asked to ChatGPT


Consider a grid of dimension n x n. A robot needs to go from cell (0, 0) to (n-1, n-1). At
each step the robot can move right or down (not left or up). 
Write a program to calculate the total number of paths that the robot can take 
from (0,0) to (n-1,n-1).
Later I asked it 
can the above problem be solved using dynamic programming?
and it gave me the same solution I had in ```unique-path.py```

"""
def factorial(num):
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def number_of_paths(n):
    """
    Calculate the number of paths the robot can take in an n x n grid from (0, 0) to (n-1, n-1).
    
    Args:
    n (int): Dimension of the grid.
    
    Returns:
    int: Total number of paths from top-left to bottom-right of the grid.
    """
    if n == 1:
        return 1
    # Number of moves: (n-1) rights and (n-1) downs, total 2(n-1)
    total_moves = 2 * (n - 1)
    moves_right = n - 1  # or moves_down, they are the same
    return binomial_coefficient(total_moves, moves_right)

# Example usage
n = int(input("Enter the dimension n of the n x n grid: "))
total_paths = number_of_paths(n)
print(f"The total number of paths from (0,0) to ({n-1},{n-1}) is {total_paths}.")
