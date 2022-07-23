def fun(ind, wt, W, val, dp):
    if ind == len(wt)-1:
        if W >= wt[ind]:
            return val[ind]
        else:
            return 0
        
    if dp[ind][W] != -1:
        return dp[ind][W]

    pick = float('-inf')
    if W-wt[ind] >=0:
        pick = val[ind] + fun(ind+1, wt, W-wt[ind], val, dp)
        
    not_pick = 0 + fun(ind+1, wt, W, val, dp)
    
    dp[ind][W] = max(pick, not_pick)
    
    return dp[ind][W]


W = 6
wt = [3, 2, 5]
val = [30, 40, 60]

dp = [[-1 for _ in range(W+1)] for _ in range(len(wt)+1)]

out = fun(ind=0, wt=wt, W=W, val=val, dp=dp)
print(out)

