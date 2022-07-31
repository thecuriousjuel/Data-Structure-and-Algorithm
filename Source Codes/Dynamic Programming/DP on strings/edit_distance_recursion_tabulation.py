def fun(s1, s2):
    n = len(s1)
    m = len(s2)
    
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = i
        
    for j in range(m+1):
        dp[0][j] = j
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 0 + dp[i-1][j-1]
                
            else:
                insert = 1 + dp[i][j-1]
                remove = 1 + dp[i-1][j]
                update = 1 + dp[i-1][j-1]
                
                dp[i][j] = min(insert, remove, update)
    
    return dp[n][m]


s1 = 'biswajit'
s2 = 'bisso'

out = fun(s1, s2)
print(out)




