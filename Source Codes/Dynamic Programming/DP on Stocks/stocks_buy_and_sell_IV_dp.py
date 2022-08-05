def fun(arr, ind, buy, k, dp):
    
    if ind == len(arr):
        return 0
    
    if k == 0:
        return 0
    
    if dp[ind][buy][k] != -1:
        return dp[ind][buy][k]
    
    # Can buy
    if buy == 1:
        profit = max(-arr[ind] + fun(arr, ind+1, 0, k, dp), 0 + fun(arr, ind+1, 1, k, dp))
        
    # Can't buy    
    else:
        profit = max(arr[ind] + fun(arr, ind+1, 1, k-1, dp), 0 + fun(arr, ind+1, 0, k, dp))
        
    dp[ind][buy][k] = profit
    return dp[ind][buy][k]



arr = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
k=7


dp = [[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(arr))]

out = fun(arr, ind=0, buy=1, k=k, dp=dp)

print(out)


