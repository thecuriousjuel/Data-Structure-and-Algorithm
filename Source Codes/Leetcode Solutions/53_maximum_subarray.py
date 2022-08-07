def fun(arr):
    max_value = arr[0]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            s = 0
            for k in range(i, j+1):
                s += arr[k]
                max_value = max(max_value, s)
    
    return max_value
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
out = fun(nums)
print(out)


