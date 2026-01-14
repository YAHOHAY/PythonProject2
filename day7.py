"""
Day 7 – Maze Path Count
Given a 2D grid of 0s and 1s:
0 means a walkable cell,
1 means an obstacle.
You start from the top-left corner (0, 0) and can move only right or down.
Your task is to count how many distinct paths can lead to the bottom-right corner (n-1, m-1).
If no valid path exists, return 0.
You should implement the logic yourself using recursion (or DFS), without using any built-in combinatorial libraries.
Bonus: add memoization to avoid recalculating overlapping subproblems.
"""
def count_paths(m, x, y):
    n1 = len(m)
    m1 = len(m[0])
    if x >= n1 or y >= m1:
        return 0
    if m[x][y] == 1:
        return 0
    if x == n1-1 and y == m1-1 :
        return 1

    down = count_paths(m, x+1, y)
    right = count_paths(m, x, y+1)
    return down + right
m = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
]
#print(count_paths(m, 0, 0))
def count_paths_memoized(m, x, y,memoized = None):
    if memoized is None:
        memoized = {}
    n1 = len(m)
    m1 = len(m[0])
    if x >= n1 or y >= m1 or m[x][y] == 1:
        return 0
    if x == n1-1 and y == m1-1 :
        return 1
    if (x,y) in memoized:
        return memoized[(x,y)]
    path = count_paths_memoized(m, x+1, y ,memoized) + count_paths_memoized(m, x, y+1, memoized)
    memoized[(x,y)] = path
    return path
print(count_paths_memoized(m, 0, 0))
"""
def dfs(state, memo=None):
    # 1️⃣ 初始化记忆表（防止默认参数陷阱）
    if memo is None:
        memo = {}

    # 2️⃣ 记忆化查找（剪枝）
    if state in memo:
        return memo[state]

    # 3️⃣ 递归终止条件（Base Case）
    if is_end(state):
        return result_of_state(state)

    # 4️⃣ 枚举所有可能的下一步状态
    best = None
    for next_state in next_states(state):
        sub_result = dfs(next_state, memo)  # 递归
        best = combine(best, sub_result)    # 处理结果（例如 min/max/累加）

    # 5️⃣ 记录结果到记忆表
    memo[state] = best
    return best

"""
