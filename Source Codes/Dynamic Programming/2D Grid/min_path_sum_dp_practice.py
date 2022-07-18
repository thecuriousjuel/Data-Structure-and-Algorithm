def fun(arr, row, col, dp):
    if row == len(arr) or col == len(arr[0]):
        return float('inf')
    
    if row == len(arr)-1 and col == len(arr[0])-1:
        return arr[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]

    left = arr[row][col] + fun(arr, row, col+1, dp)
    down = arr[row][col] + fun(arr, row+1, col, dp)
    
    dp[row][col] = min(left, down)
    
    return dp[row][col]


arr = [[5,9,6],
       [11,5,2]]

dp = [[-1 for _ in range(len(arr[0])+1)] for _ in range(len(arr))]

out = fun(arr, row=0, col=0, dp=dp)
print(out)


