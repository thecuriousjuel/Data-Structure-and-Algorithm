def fun(arr, ind, dp):
    if ind == 0:
        return arr[ind]
    
    if ind < 0:
        return 0
    
    if ind in dp:
        return dp[ind]
    
    pick = arr[ind] + fun(arr, ind-2, dp)
    not_pick = 0 + fun(arr, ind-1, dp)
    
    dp[ind] = max(pick, not_pick)
    
    return dp[ind]


nums = [2, 1, 3, 9]
n = len(nums)
dp = {}

l = fun(nums[:-1], n-1-1, dp)
r = fun(nums[1:], n-1-1, dp)

print(max(l, r))

    
