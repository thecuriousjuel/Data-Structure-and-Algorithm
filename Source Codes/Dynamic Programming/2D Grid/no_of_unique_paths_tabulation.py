def fun(row, col):    
    dp = [[-1 for _ in range(col)] for _ in range(row)]
    
    dp[0][0] = 1
    
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue
            
            up = 0
            if i > 0:
                up = dp[i-1][j]
                    
            left = 0
            if j > 0:
                left = dp[i][j-1]
                
            dp[i][j] = left + up
                
    print(dp)
                
    return dp[row-1][col-1]

row = 3
col = 2
out = fun(row, col)
print(out)




