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


def array_check(arr):
    n = len(arr)
    s = 0
    for i in arr:
        s += i

    if s % 2 != 0:
        return False
    
    target = s / 2

    out = fun(arr, n-1, target)
    return out

arr = [1,2,3,4,1,2,3]
print(array_check(arr))


