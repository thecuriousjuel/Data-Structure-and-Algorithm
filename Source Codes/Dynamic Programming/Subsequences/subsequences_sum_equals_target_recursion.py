def fun(arr, ind, target):
    
    if target == 0:
        return True
    
    if ind == 0:
        return arr[ind] == target
 
    not_take = fun(arr, ind-1, target)
    
    take = False
    if arr[ind] <= target: 
        take = fun(arr, ind-1, target-arr[ind])
    
    return not_take or take


arr = [1,2,3,4]
n = len(arr)
target = 11

out = fun(arr, n-1, target)

print(out)

