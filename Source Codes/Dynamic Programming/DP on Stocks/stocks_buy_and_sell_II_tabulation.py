def fun(arr):
    
    n = len(arr)
    
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    
    for ind in range(n-1, -1, -1):
        for buy in range(2):

            if buy == True:
                profit = max(-arr[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
                             
            else:
                profit = max(arr[ind] + dp[ind+1][1], 0 + dp[ind+1][0])
                             
            dp[ind][buy] = profit
            
    return dp[ind][buy]


arr = [7,1,5,3,6,4]
out = fun(arr)
print(out)


