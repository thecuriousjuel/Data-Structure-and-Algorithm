def fun(arr, ind, dp):
    if ind == 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    one_step = fun(arr, ind-1, dp) + abs(arr[ind] - arr[ind-1])
    two_step = float('inf')
    
    if ind - 2 >= 0:
        two_step = fun(arr, ind-2, dp) + abs(arr[ind] - arr[ind-2])

    return min(one_step, two_step)


arr = [10, 20, 30, 10, 20, 30]

dp = [-1 for i in range(len(arr)+1)]

ind = len(arr)-1

out = fun(arr, ind, dp)
print(out)
    
