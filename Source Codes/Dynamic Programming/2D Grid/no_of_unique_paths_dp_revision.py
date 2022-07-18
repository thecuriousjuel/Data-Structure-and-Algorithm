def fun(arr, row, col, dp):
    
    if col == len(arr[0]):
        return 0
    
    if row == len(arr):
        return 0
    
    if row == len(arr)-1 and col == len(arr[0])-1:
        return 1
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    right = fun(arr, row, col+1, dp)
    down = fun(arr, row+1, col, dp)
    
    dp[row][col] = right + down
    return dp[row][col]


n = 10

arr = [[1 for _ in range(n)] for _ in range(n)]
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

out = fun(arr, row=0, col=0, dp=dp)

print(out)