def fun(arr, n, k, dp):
    if n == 0:
        return 0

    if dp[n] != -1:
        return dp[n]

    min_energy = float('inf')
    for i in range(1, k+1):
        if n-i >=0:
            out = fun(arr, n-i, k, dp) + abs(arr[n] - arr[n-i])
            min_energy = min(min_energy, out)
    
    dp[n] = min_energy

    return dp[n]
    
    
arr = [30, 10, 60, 10, 60, 50]
n = len(arr)

dp = [-1 for _ in range(n)]
k = 5
out = fun(arr, n-1, k, dp)
print(out)
