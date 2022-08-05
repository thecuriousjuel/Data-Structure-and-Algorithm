def fun(arr, ind, dp):

    if ind == 0:
        return arr[ind]
    
    if dp[ind] != -1:
        return dp[ind]
    
    rob = 0
    if ind-2 >= 0:
        rob = arr[ind] + fun(arr, ind-2, dp)
    not_rob = 0 + fun(arr, ind-1, dp)
    
    dp[ind] = max(rob, not_rob)
    
    return dp[ind]


arr = [1,2,3,1]
#arr = [2,7,9,3,1]

ind = len(arr)

dp = [-1 for _ in range(ind)]

out = fun(arr, ind-1, dp)
print(out)
print(dp)
