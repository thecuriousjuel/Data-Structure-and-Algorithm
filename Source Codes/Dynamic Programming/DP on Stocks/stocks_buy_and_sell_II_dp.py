def fun(arr, ind, buy, dp):
    if ind == len(arr):
        return 0
    
    if dp[ind][buy] != -1:
        return dp[ind][buy]

    if buy == True:
        profit = max(-arr[ind] + fun(arr, ind+1, False, dp), 0 + fun(arr, ind+1, True, dp))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, True, dp), 0 + fun(arr, ind+1, False, dp))
        
    dp[ind][buy] = profit
    
    return dp[ind][buy]


arr = [7,1,5,3,6,4]
ind = 0

dp = [[-1 for _ in range(2)] for _ in range(len(arr))]

out = fun(arr, ind, True, dp)
print(out)

