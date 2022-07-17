def fun(arr, ind, k, dp):
    if ind == 0:
        return 0
    
    if dp[ind] != -1:
        return dp[ind]
    
    min_value = float('inf')
    
    for i in range(1, k+1):
        if ind - i >= 0:
            steps = fun(arr, ind-i, k, dp) + abs(arr[ind] - arr[ind - i])

        min_value = min(min_value, steps)

    dp[ind] = min_value
    return dp[ind]


arr = [10, 20, 30, 10, 50, 30]
dp = [-1 for i in range(len(arr))]
ind = len(arr)-1
k = 3

out = fun(arr, ind, k, dp)
print(out)
    
