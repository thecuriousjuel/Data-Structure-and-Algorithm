def fun(arr, n, k, dp={}):
    dp[0] = 0

    for i in range(1, n):
        min_steps = float('inf')

        for j in range(1, k+1):
            if i-j >= 0:
                jump = dp[i-j] + abs(arr[i] - arr[i-j])
                min_steps = min(min_steps, jump)
        
        dp[i] = min_steps

    return dp[n-1]

arr = [10, 20, 30, 10, 60, 20]
n = len(arr)
k = 4

print(fun(arr, n, k))

