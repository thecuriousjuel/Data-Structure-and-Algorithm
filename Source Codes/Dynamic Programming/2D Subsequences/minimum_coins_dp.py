def fun(arr, ind, t, dp):
    #print(ind, t)
    
    if ind == len(arr)-1:
        if t % arr[ind] == 0:
            return t // arr[ind]
        return float('inf')
    
    if dp[ind][t] != -1:
        return dp[ind][t]

    pick = float('inf')
    if t-arr[ind] >= 0:
        pick = 1 + fun(arr, ind, t-arr[ind], dp)
        
    not_pick = 0 + fun(arr, ind+1, t, dp)
    
    dp[ind][t] = min(pick, not_pick)
    
    return dp[ind][t]
    

arr = [1,3]
t = 11

dp = [[-1 for _ in range(t+1)] for _ in range(len(arr)+1)]

out = fun(arr, ind=0, t=t, dp=dp)
print(out)


