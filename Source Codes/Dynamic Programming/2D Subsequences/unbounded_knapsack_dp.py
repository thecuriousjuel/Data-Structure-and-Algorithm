def fun(wt, val, ind, W, dp):
    if W == 0:
        return 0
    
    if ind == len(wt):
        return float('-inf')
    
    if dp[ind][W] != -1:
        return dp[ind][W]
    
    pick = float('-inf')
    if W-wt[ind] >= 0:
        pick = val[ind] + fun(wt, val, ind, W-wt[ind], dp)

    not_pick = 0 + fun(wt, val, ind+1, W, dp)
    
    dp[ind][W] = max(pick, not_pick)
    
    return dp[ind][W]


wt = [1, 3, 4, 5]
val = [10, 40, 50, 70]
W = 8

dp = [[-1 for _ in range(W+1)] for _ in range(len(wt))]

out = fun(wt, val, ind=0, W=W, dp=dp)
print(out)


