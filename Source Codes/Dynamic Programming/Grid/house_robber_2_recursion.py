def fun(arr, ind):
    if ind == 0:
        return arr[ind]
    
    if ind < 0:
        return 0
    
    pick = arr[ind] + fun(arr, ind-2)
    not_pick = 0 + fun(arr, ind-1)
    
    return max(pick, not_pick)


nums = [2, 1, 3, 9, 3]
n = len(nums)

l = fun(nums[:-1], n-2)
r = fun(nums[1:], n-2)

print(max(l, r))

    
