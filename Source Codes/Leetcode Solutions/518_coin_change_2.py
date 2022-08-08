def fun(arr, k):
    
    l = len(arr)
    
    dp = [[0 for _ in range(amount+1)] for _ in range(l)]
        
    for k in range(amount+1):
        if k % arr[0] == 0:
            dp[0][k] = 1
        else:
            dp[0][k] = 0
    
    
    for ind in range(1, l):
        for k in range(amount+1):
            pick = 0
            if k-arr[ind] >= 0:
                pick = dp[ind][k-arr[ind]]
            
            not_pick = dp[ind-1][k]
            
            dp[ind][k] = pick + not_pick
            
    
    return dp[l-1][k]


arr = [2, 5]
amount = 5

out = fun(arr, amount)

print(out)
