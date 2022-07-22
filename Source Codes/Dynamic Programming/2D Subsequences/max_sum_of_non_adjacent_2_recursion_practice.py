def fun(arr, ind):
    if ind == 0:
        return arr[ind]
    
    if ind < 0:
        return 0
    
    pick = arr[ind] + fun(arr, ind-2)
    
    not_pick = 0 + fun(arr, ind-1)

    return max(pick, not_pick)


arr = [2, 1, 4, 9] 
ind = len(arr)

dp = [-1 for _ in range(ind+1)]

out = fun(arr, ind-1)
print(out)

