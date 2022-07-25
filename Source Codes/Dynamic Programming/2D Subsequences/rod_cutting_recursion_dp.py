def fun(price, ind, N, dp):
    
    if N == 0:
        return 0
    
    if ind == len(price):
        return float('-inf')
    
    if dp[ind][N] != -1:
        return dp[ind][N]
    
    pick = float('-inf')
    if N-(ind+1) >= 0:   
        pick = price[ind] + fun(price, ind+1, N-(ind+1), dp)
    not_pick = 0 + fun(price, ind+1, N, dp)

    dp[ind][N] = max(pick, not_pick)
    
    return dp[ind][N]


price = [2,5,7,8,10]

N = len(price)

dp = [[-1 for _ in range(N+1)] for _ in range(N)]

out = fun(price, ind=0, N=N, dp=dp)

print(out)


