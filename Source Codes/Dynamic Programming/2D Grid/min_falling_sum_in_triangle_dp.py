def fun(tri, row, col, dp):
    
    if row == len(tri) - 1:
        return tri[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    down = tri[row][col] + fun(tri, row+1, col, dp)
    right_diag = tri[row][col] + fun(tri, row+1, col+1, dp)
    
    dp[row][col] = min(down, right_diag)
    
    return dp[row][col]


tri = [[1],
       [2, 3],
       [3, 6, 7],
       [8, 9, 6, 10]]

row = 0
col = 0

dp = [[-1 for _ in range(len(tri))] for _ in range(len(tri))]
out = fun(tri, row, col, dp)

print('Final : ', out)

