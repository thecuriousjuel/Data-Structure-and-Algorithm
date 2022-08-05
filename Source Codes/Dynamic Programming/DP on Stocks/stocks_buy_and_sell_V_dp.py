def fun(arr, ind, buy, dp):
    
    if ind >= len(arr):
        return 0
    
    if dp[ind][buy] != -1:
        return dp[ind][buy]
    
    if buy == 1:
        profit = max(-arr[ind] + fun(arr, ind+1, 0, dp),
                     0 + fun(arr, ind+1, 1, dp))
    else:
        profit = max(arr[ind] + fun(arr, ind+2, 1, dp),
                     0 + fun(arr, ind+1, 0, dp))
    
    dp[ind][buy] = profit
    return dp[ind][buy]


price = [4,9,0,4,10]
ind = 0
buy = 1

dp = [[-1 for _ in range(2)] for _ in range(len(price))]

out = fun(price, ind, buy, dp)
print(out)

