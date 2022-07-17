def fun(ind, dp):
    if ind <= 1:
        return 1
    
    if dp[ind] != -1:
        return dp[ind]
    
    one_step = fun(ind-1, dp)
    two_step = fun(ind-2, dp)
    
    dp[ind] = one_step + two_step
    return dp[ind]


n = 40
dp = [-1 for i in range(n+1)]

out = fun(n, dp)

print(out)
