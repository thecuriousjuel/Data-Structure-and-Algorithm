def fun(arr, ind, k, dp):
    # print(k)
    if k == 0:
        return True
    
    if ind == len(arr)-1:
        return False
    
    if dp[ind][k] != -1:
        return arr[ind][k]
    
    pick = False
    if k >= arr[ind]:
        pick = fun(arr, ind+1, k-arr[ind], dp)
        if pick:
            return pick
        
    not_pick = fun(arr, ind+1, k, dp)
    if not_pick:
        return not_pick
    
    dp[ind][k] = pick or not_pick
    
    return dp[ind][k]


arr = [1,2,3,4]
k = 4

dp = [[-1 for _ in range(len(arr)+1)] for _ in range(k+1)]

out = fun(arr, ind=0, k=k, dp=dp)

print(out)

