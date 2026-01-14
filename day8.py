"""
Given an m x n grid filled with non-negative numbers,
find a path from the top-left to the bottom-right
that minimizes the sum of all numbers along its path.
You can only move right or down at any point in time.
Use recursion with memoization, not iteration.
Example:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
Output:
7
"""
def minimal_sum(grid,x = 0,y = 0,memo = None):
    if memo is None:
        memo = {}
    n = len(grid) #行
    m = len(grid[0]) #列
    if x >= m or y >= n:
        return float('inf')
    if x == m -1 and y == n-1:
        return grid[y][x]
    if (x, y) in memo:
        return memo[(x, y)]
    right = minimal_sum(grid,x+1,y,memo)
    down = minimal_sum(grid,x,y+1,memo)
    memo[(x,y)] = min(right,down) + grid[y][x]
    return memo[(x,y)]


grid = [
    [1, 3, 1],
    [1, 5, 1],
]
print(minimal_sum(grid))