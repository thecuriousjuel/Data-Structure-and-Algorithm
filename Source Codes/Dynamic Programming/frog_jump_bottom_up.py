def fun(arr, n, dp={}):
    dp[0] = 0
    right = float('inf')

    for i in range(1, n):
        left = dp[i-1] + abs(arr[i] - arr[i-1])
        
        if i > 1:
            right = dp[i-2] + abs(arr[i] - arr[i-2])

        dp[i] = min(left, right)
        
        print(dp)

    return dp[n-1]

arr = [10, 20, 30, 10, 60]
n = len(arr)

print(fun(arr, n))


