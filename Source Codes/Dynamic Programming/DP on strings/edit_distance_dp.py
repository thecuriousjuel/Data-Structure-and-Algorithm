def fun(s1, s2, i, j, dp):
    
    if i < 0:
        return j+1
    
    if j < 0:
        return i+1
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s1[i] == s2[j]:
        dp[i][j] = 0 + fun(s1, s2, i-1, j-1, dp)
        return dp[i][j]
    
    insert = 1 + fun(s1, s2, i, j-1, dp)
    remove = 1 + fun(s1, s2, i-1, j, dp)
    update = 1 + fun(s1, s2, i-1, j-1, dp)
    
    dp[i][j] = min(insert, remove, update)
    
    return dp[i][j]


s1 = 'horse'
s2 = 'ros'

n = len(s1)
m = len(s2)

dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

out = fun(s1, s2, n-1, m-1, dp)
print(out)
print(dp)

