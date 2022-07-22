def fun(arr, ind, path, target):
    if target == 0:
        # print(path)
        return True
    
    if target < 0:
        return False
    
    if ind == len(arr)-1:
        return arr[ind] == target

    if dp[ind][target] != -1:
        return dp[ind][target]
    
    path.append(arr[ind])
    left = fun(arr, ind+1, path, target-arr[ind])
    path.pop()
    
    right = fun(arr, ind+1, path, target)

    dp[ind][target] = left or right
    return dp[ind][target]

arr = [4, 1, 3, 2, 1, 5, 6, 4, 7, 9, 2, 5, 7, 8, 9]
ind = 0
path = []
target = 11

dp = [[-1 for _ in range(target+1)] for _ in range(len(arr))]

print(fun(arr, ind, path, target))

