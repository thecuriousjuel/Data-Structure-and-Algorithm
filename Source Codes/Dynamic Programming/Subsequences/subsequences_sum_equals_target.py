def fun(arr, target, ind, ans, s=0):
    
    if ind == len(arr):
        if s == target:
            return True
        return False


    out1 = fun(arr, target, ind+1, ans, s+arr[ind])
    
    out2 = fun(arr, target, ind+1, ans, s)
    
    return out1 or out2
    
    
arr = [1,2,3,4]
target = 11
ans = []

out = fun(arr, target, 0, ans)

print(out)
