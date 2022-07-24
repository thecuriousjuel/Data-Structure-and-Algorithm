def fun(arr, ind, t, dp):
    
    if t == 0:
        return 1
    
    if ind == len(arr):
        return 0
    
    if dp[ind][t] != -1:
        return dp[ind][t]
        
    pick = 0
    if t-arr[ind] >= 0:
        pick = fun(arr, ind, t-arr[ind], dp)
        
    not_pick = fun(arr, ind+1, t, dp)
    
    dp[ind][t] = pick + not_pick
    
    return dp[ind][t]


arr = [1,2,5]
t = 4

dp = [[-1 for _ in range(t+1)] for _ in range(len(arr))]

out = fun(arr, ind=0, t=t, dp=dp)
print(out)

