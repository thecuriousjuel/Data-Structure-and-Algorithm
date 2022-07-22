def fun(arr, ind, target):    
    if target == 0:
        return True
    
    if ind == 0:
        return arr[ind] == target
    
    not_take = fun(arr, ind-1, target)

    take = False
    if target >= arr[ind]: 
        take = fun(arr, ind-1, target-arr[ind])
      
    return not_take or take


arr = [4, 1, 3, 2]
n = len(arr)
target = 11

out = fun(arr, n-1, target)

print(out)

