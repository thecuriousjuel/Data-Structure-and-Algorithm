def fun(arr, ind):
    if ind == 0:
        return 0
    
    one_step = fun(arr, ind-1) + abs(arr[ind] - arr[ind-1])
    two_step = float('inf')
    
    if ind - 2 >= 0:
        two_step = fun(arr, ind-2) + abs(arr[ind] - arr[ind-2])
    
    print(f'index={ind} left={one_step} right={two_step}')
    return min(one_step, two_step)


arr = [10, 20, 30, 10]
ind = len(arr)-1

out = fun(arr, ind)
print(out)
    
