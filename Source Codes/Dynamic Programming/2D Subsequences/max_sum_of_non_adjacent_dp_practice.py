def fun(arr, ind, dp):
    if ind == 0:
        return arr[ind]
    
    if ind < 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    
    pick = arr[ind] + fun(arr, ind-2, dp)
    
    not_pick = 0 + fun(arr, ind-1, dp)
    
    dp[ind] = max(pick, not_pick)
    
    return dp[ind]


arr = [2, 1, 4, 9] 
ind = len(arr[1:])

dp = [-1 for _ in range(ind+1)]

out = fun(arr, ind, dp)
print(out)









