"""
Space Optimization is not done but optimized time complexity solution is coded below.

"""


def fun(arr):
    
    dp = [[0 for _ in range(2)] for _ in range(len(arr)+2)]
    
    for ind in range(len(arr)-1, -1, -1):
        dp[ind][1] = max(-arr[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
        dp[ind][0] = max(arr[ind] + dp[ind+2][1], 0 + dp[ind+1][0])
            
    return dp[ind][1]


prices = [4,9,0,4,10]

out = fun(prices)
print(out)



