def fun(arr, ind, path, target, dp):
    if target == 0:
        # print(path)
        return True
    
    if target < 0:
        return False
    
    if ind == len(arr):
        return

    if dp[ind][target] != -1:
        return dp[ind][target]
    
    path.append(arr[ind])
    left = fun(arr, ind+1, path, target-arr[ind], dp)

    path.pop()
    
    right = fun(arr, ind+1, path, target, dp)

    dp[ind][target] = left or right

    return dp[ind][target]


arr = [2, 3, 3, 3, 4, 5]
ind = 0
path = []

s = sum(arr)
if s % 2 != 0:
    print('False')
else:
    target = s // 2
    dp = [[-1 for _ in range(target+1)] for _ in range(len(arr))]
    print(fun(arr, ind, path, target, dp))

