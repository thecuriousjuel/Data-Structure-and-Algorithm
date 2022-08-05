def fun(arr):
    
    i = len(arr)
    j = 2
    k = 2
    

    dp = [[[0 for _ in range(k+1)] for _ in range(j)] for _ in range(i+1)]
    
    for ind in range(i-1, -1, -1):
        for buy in range(j):
            for count in range(1, k+1):

                if buy:
                    profit = max(-arr[ind] + dp[ind+1][0][count],
                                 0 + dp[ind+1][1][count])
                else:
                    profit = max(arr[ind] + dp[ind+1][1][count-1],
                                 0 + dp[ind+1][0][count])
                    
                dp[ind][buy][count] = profit
                
    return dp[0][1][2]



arr = [3,3,5,0,0,3,1,4]
out = fun(arr)
print(out)


