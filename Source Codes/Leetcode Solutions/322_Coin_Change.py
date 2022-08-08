def fun(arr, ind, k, dp):
    
    if k == 0:
        return 0
    
    if ind == -1:
        return float('inf')
    
    if dp[ind][k] != -1:
        return dp[ind][k]

    pick = float('inf')
    
    if k-arr[ind] >= 0:
        pick = 1 + fun(arr, ind, k-arr[ind], dp)
    not_pick = 0 + fun(arr, ind-1, k, dp)
    
    dp[ind][k] = min(pick, not_pick)
    
    return dp[ind][k]



coins = [3,7,405,436]
amount = 8839

ind = len(coins)
dp = [[-1 for _ in range(amount+1)] for _ in range(ind)]

out = fun(coins, ind-1, amount, dp)
if out == float('inf'):
    out = -1
print(out)

