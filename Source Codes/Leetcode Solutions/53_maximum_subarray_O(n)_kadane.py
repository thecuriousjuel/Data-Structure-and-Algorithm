def fun(arr):
    max_value = arr[0]
    s = 0
    
    for i in range(len(arr)):
        s += arr[i]
        max_value = max(max_value, s)
        
        if s < 0:
            s = 0
    
    return max_value
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
out = fun(nums)
print(out)


