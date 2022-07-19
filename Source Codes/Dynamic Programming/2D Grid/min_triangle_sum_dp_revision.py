def fun(arr, row, col, dp):
    
    if row == len(arr)-1:
        return arr[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]

    down = arr[row][col] + fun(arr, row+1, col, dp)
    right_diag = arr[row][col] + fun(arr, row+1, col+1, dp)

    dp[row][col] = min(down, right_diag)
    return dp[row][col]


arr = [[1],
       [2,3],
       [3,6,7],
       [8,9,6,10]]

dp = [[-1 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
out = fun(arr, row=0, col=0, dp=dp)

print(out)