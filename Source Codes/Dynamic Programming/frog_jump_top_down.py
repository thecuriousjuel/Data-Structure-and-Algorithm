def fun(arr, n, dp={}):
    if n == 0:
        return 0


    if n in dp:
        return dp[n]
    
    left = fun(arr, n-1) + abs(arr[n] - arr[n-1])
    right = float('inf')
    
    if n > 1:
        right = fun(arr, n-2) + abs(arr[n] - arr[n-2])

    dp[n] = min(left, right)

    return dp[n]


arr = [10, 20, 30, 10, 60]
n = len(arr)

print(fun(arr, n-1))


