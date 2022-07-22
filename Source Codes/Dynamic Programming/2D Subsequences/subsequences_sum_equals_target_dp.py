def fun(arr, ind, target, dp):
    
    if target == 0:
        return True
    
    if ind == 0:
        return arr[ind] == target
    
    if dp[ind][target] != -1:
        return dp[ind][target]
 
    not_take = fun(arr, ind-1, target, dp)
    
    take = False
    if arr[ind] <= target: 
        take = fun(arr, ind-1, target-arr[ind], dp)
    
    dp[ind][target] = not_take or take
    
    return dp[ind][target]


arr = [1,2,3,4]
n = len(arr)
target = 10

dp = [[-1 for _ in range(target+1)] for _ in range(n)]

out = fun(arr, n-1, target, dp)

print(out)

