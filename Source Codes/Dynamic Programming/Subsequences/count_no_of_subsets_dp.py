def fun(arr, ind, target, path, dp):
    if target == 0:
        # print(path)
        return 1
        
    if target < 0:
        return 0
    
    if ind == len(arr):
        return 0
    
    if dp[ind][target] != -1:
        return dp[ind][target]

    path.append(arr[ind])
    pick = fun(arr, ind+1, target-arr[ind], path, dp)
    path.pop()
    
    not_pick = fun(arr, ind+1, target, path, dp)
    
    dp[ind][target] = pick + not_pick

    return dp[ind][target]


#arr = [1, 2, 2, 3, 5, 6]
arr = [0, 0, 1]
ind = 0
target = 6
path = []

dp = [[-1 for _ in range(target+1)] for _ in range(len(arr))]

out = fun(arr, ind, target, path, dp)
print(out)

        

