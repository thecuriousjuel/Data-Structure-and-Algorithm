def fun(arr, ind, k, dp):
    if k == 0:
        return 1
    
    if ind >= len(arr):
        return 0
    
    if dp[ind][k] != -1:
        return dp[ind][k]
    
    pick = 0
    if k >= arr[ind]:
        pick = fun(arr, ind+1, k-arr[ind], dp)
        
    not_pick = fun(arr, ind+1, k, dp)
    
    dp[ind][k] = pick + not_pick
    
    return dp[ind][k]
    

arr = [0,0,1]
k=1
dp = [[-1 for _ in range(k+1)] for _ in range(len(arr)+1)]

out = fun(arr, ind=0, k=k, dp=dp)

print(out)
