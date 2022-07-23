def fun(arr, n):
    dp = [-1 for _ in range(n)]
    dp[0] = arr[0]
    
    for ind in range(1, n):
        
        if ind > 1:
            pick = arr[ind] + dp[ind-2]
        else:
            pick = arr[ind]
    
        not_pick = 0 + dp[ind-1]
    
        dp[ind] = max(pick, not_pick)
        
    return dp[n-1]
        
        
arr = [2, 1, 4, 9]
n = len(arr)

out = fun(arr, n)
print(out)









