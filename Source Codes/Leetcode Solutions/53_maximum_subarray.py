def fun(arr, ind):
    
    if ind == 0:
        return arr[ind]
    
    pick = arr[ind] + fun(arr, ind-1)
    not_pick = 0 + fun(arr, ind-1)
    
    return max(pick, not_pick)
    
    

nums = [5,4,-1,7,8]

out = fun(nums, len(nums)-1)

print(out)

