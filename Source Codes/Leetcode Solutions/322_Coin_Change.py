def fun(arr, amount):
    
    l = len(arr)
    
    dp = [[0 for _ in range(amount+1)] for _ in range(l)]
    
    for k in range(amount+1):
        if k % arr[0] == 0:
            dp[0][k] = k // arr[0]
        else:
            dp[0][k] = float('inf')
        
    pick = float('inf')
    
    for ind in range(1, l):
        for k in range(amount+1):
            
            if k-arr[ind] >= 0:
                pick = 1 + dp[ind][k-arr[ind]]
                
            not_pick = 0 + dp[ind-1][k]
            
            dp[ind][k] = min(pick, not_pick)
    
    return dp[l-1][k]



coins = [2,5]
amount = 9

out = fun(coins, amount)
if out == float('inf'):
    out = -1
print(out)

