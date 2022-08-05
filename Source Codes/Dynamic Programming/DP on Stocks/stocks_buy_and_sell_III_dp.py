def fun(arr, ind, buy, count, dp):
    
    if count == 0 or ind == len(arr):
        return 0
    
    if dp[ind][buy][count] != -1:
        return dp[ind][buy][count]

    if buy:
        profit = max(-arr[ind] + fun(arr, ind+1, 0, count, dp),
                     0 + fun(arr, ind+1, 1, count, dp))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, 1, count-1, dp),
                     0 + fun(arr, ind+1, 0, count, dp))
        
    dp[ind][buy][count] = profit
    return dp[ind][buy][count]


arr = [3,3,5,0,0,3,1,4]
ind = 0
count = 2

dp = [[[-1 for _ in range(count+1)] for _ in range(2)] for _ in range(len(arr))]

out = fun(arr, ind, 1, count, dp)
print(out)

