def fun(arr, n):
    prev1 = arr[0]
    prev2 = 0
    
    for ind in range(1, n):
        
        if ind > 1:
            pick = arr[ind] + prev2
        else:
            pick = arr[ind]
    
        not_pick = 0 + prev1
    
        curi = max(pick, not_pick)
        
        prev2 = prev1
        prev1 = curi
        
    return prev1
        
        
arr = [2, 1, 4, 9]
n = len(arr)

out = fun(arr, n)
print(out)









