def fun(arr):
    max_value = arr[0]
    for i in range(len(arr)):
        s = 0
        for j in range(i, len(arr)):
            s += arr[j]
            max_value = max(max_value, s)
    
    return max_value
    

nums = [5,4,-1,7,8]
out = fun(nums)
print(out)



