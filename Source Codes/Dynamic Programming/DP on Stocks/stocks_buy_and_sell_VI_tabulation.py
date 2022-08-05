def fun(arr):
    dp = [[0 for _ in range(2)] for _ in range(len(arr)+1)]
    
    for ind in range(len(arr)-1, -1, -1):
        for buy in range(2):
    
            if buy == 1:
                dp[ind][buy] = max(-arr[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
            else:
                dp[ind][buy] = max(-fee + arr[ind] + dp[ind+1][1], 0 + dp[ind+1][buy])

    return dp[0][1]


price = [4,9,0,4,10]
ind = 0
buy = 1
fee = 2

out = fun(price)
print(out)



