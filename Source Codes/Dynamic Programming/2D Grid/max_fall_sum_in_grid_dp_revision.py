def fun(arr, n, m, row, col, dp):
    #print(f'row={row}, col={col}')
    
    if col < 0 or col >= m:
        return float('-inf')
    
    if row == n-1:
        return arr[row][col]
    
    if dp[row][col] != -1:
        return dp[row][col]
    
    left_diag = arr[row][col] + fun(arr, n, m, row+1, col-1, dp)
    down = arr[row][col] + fun(arr, n, m, row+1, col, dp)
    right_diag = arr[row][col] + fun(arr, n, m, row+1, col+1, dp)
    
    dp[row][col] = max(down, left_diag, right_diag)
    
    return dp[row][col] 

arr = [[1,2,10,4],
       [100,3,2,1],
       [1,1,20,2],
       [1,2,2,1]]

n = len(arr)
m = len(arr[0])

dp = [[-1 for _ in range(m)] for _ in range(n)]

row = 0

maxi = float('-inf')
for i in range(len(arr[row])):
    s = fun(arr, n, m, row, i, dp)
    maxi = max(maxi, s)
    
print(maxi)

