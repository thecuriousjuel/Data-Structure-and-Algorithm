def fun(s1, s2, i, j, dp):
    
    if i == 0:
        return j
    
    if j == 0:
        return i
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s1[i-1] == s2[j-1]:
        dp[i][j] = 0 + fun(s1, s2, i-1, j-1, dp)
        return dp[i][j]
    
    insert = 1 + fun(s1, s2, i, j-1, dp)
    remove = 1 + fun(s1, s2, i-1, j, dp)
    update = 1 + fun(s1, s2, i-1, j-1, dp)
    
    dp[i][j] = min(insert, remove, update)
    
    return dp[i][j]


s1 = 'biswajit'
s2 = 'bisso'

n = len(s1)
m = len(s2)

dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

out = fun(s1, s2, n, m, dp)
print(out)
#print(dp)

