def fun(grid, row, col, dp):
    
    if row == len(grid) or col == len(grid[0]):
        return 0

    if grid[row][col] == -1:
        return 0

    if row == len(grid)-1 and col == len(grid[0])-1:
        return 1
    
    if dp[row][col] != -1:
        return dp[row][col]

    right = fun(grid, row, col+1, dp)
    down = fun(grid, row+1, col, dp)

    return right + down

N = 5
M = 3

row = 0
col = 0

grid = [[0 for _ in range(M)] for _ in range(N)]
grid[1][1] = -1
grid[1][2] = -1

dp = [[-1 for _ in range(M)] for _ in range(N)]

print(fun(grid, row, col, dp))