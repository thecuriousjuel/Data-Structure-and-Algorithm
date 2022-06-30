def fun(grid, r, c, i, j1, j2, dp):
    if j1 < 0 or j1 >= c or j2 < 0 or j2 >= c:
        return float('-inf')
    
    
    if i == r-1:
        if j1 == j2:
            return grid[i][j1]
        
        else:
            return grid[i][j1] + grid[i][j2]
        
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
        
    
    maxi = float('-inf')
    for di in range(-1, 2):
        for dj in range(-1, 2):
            value = 0
            if j1 == j2:
                value = grid[i][j1]
            else:
                value = grid[i][j1] + grid[i][j2]
                
            value += fun(grid, r, c, i+1, j1+di, j2+dj, dp)
            maxi = max(maxi, value)
        
    dp[i][j1][j2] = maxi
    return dp[i][j1][j2]



grid = [[2, 3, 1, 2],
        [3, 4, 2, 2],
        [5, 6, 3, 5]]

r = len(grid)
c = len(grid[0])

i = 0
j1 = 0
j2 = c-1

dp = [[[-1 for _ in range(c)] for _ in range(c)] for _ in range(r)]

print(fun(grid, r, c, i, j1, j2, dp))


