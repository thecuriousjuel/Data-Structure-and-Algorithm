def fun(arr, kk):
    
    dp = [[[0 for _ in range(kk+1)] for _ in range(2)] for _ in range(len(arr)+1)]

    
    for ind in range(len(arr)-1, -1, -1):
        for buy in range(2):
            for k in range(1, kk+1):
    
                # Can buy
                if buy == 1:
                    profit = max(-arr[ind] + dp[ind+1][0][k], 0 + dp[ind+1][1][k])
                    
                # Can't buy    
                else:
                    profit = max(arr[ind] + dp[ind+1][1][k-1], 0 + dp[ind+1][0][k])
                    
                dp[ind][buy][k] = profit
                
    return dp[0][1][kk]



arr = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
kk=7

out = fun(arr, kk)
print(out)


