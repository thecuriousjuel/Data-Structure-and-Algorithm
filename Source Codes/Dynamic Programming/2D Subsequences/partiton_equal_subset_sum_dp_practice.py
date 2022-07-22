def fun(arr, ind, k, dp):
    if k == 0:
        return True
    
    if ind >= len(arr)-1:
        return False
    
    if dp[ind][k] != -1:
        return dp[ind][k]

    pick = False
    if k-arr[ind] >= 0:
        pick = fun(arr, ind+1, k-arr[ind], dp)
        if pick == True:
            return True
    
    not_pick = fun(arr, ind+1, k, dp)
    if not_pick == True:
        return True
    
    dp[ind][k] = pick or not_pick
    
    return dp[ind][k]


arr = [2,8,6]
s = 0
ind = 0

for i in arr:
    s += i
    
k = s//2

dp = [[-1 for _ in range(k+1)] for _ in range(len(arr)+1)]
    
if s % 2 == 0:
    out = fun(arr, ind, k, dp)
else:
    out = False
    
print(out)

