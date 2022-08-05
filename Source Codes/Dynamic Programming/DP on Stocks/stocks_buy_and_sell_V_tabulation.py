def fun(arr):
    
    dp = [[0 for _ in range(2)] for _ in range(len(arr)+2)]
    
    for ind in range(len(arr)-1, -1, -1):
        for buy in range(2):
    
            if buy == 1:
                profit = max(-arr[ind] + dp[ind+1][0],
                             0 + dp[ind+1][1])
            else:
                profit = max(arr[ind] + dp[ind+2][1],
                             0 + dp[ind+1][0])
            
            dp[ind][buy] = profit
    return dp[ind][buy]


prices = [4,9,0,4,10]

out = fun(prices)
print(out)


