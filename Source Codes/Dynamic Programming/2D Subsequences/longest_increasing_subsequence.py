def fun(arr, ind, prev, dp):
    
    if ind == len(arr):
        return 0
    
    if dp[ind][prev+1] != -1:
        return dp[ind][prev+1]
    
    not_pick = 0 + fun(arr, ind+1, prev, dp)
    
    pick = 0
    if prev == -1 or arr[ind] > arr[prev]:
        pick = 1 + fun(arr, ind+1, ind, dp)
    
    dp[ind][prev+1] = max(pick, not_pick)
    return dp[ind][prev+1]
    

arr = [0,1,0,3,2,3]
ind = 0
prev = -1

n = len(arr)
        
dp = [[-1 for _ in range(n)] for _ in range(n)]

out = fun(arr, ind, prev, dp)
print(out)


