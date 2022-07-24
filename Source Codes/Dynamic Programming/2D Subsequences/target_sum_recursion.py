def fun(arr, ind, t, path=[]):
    if ind == len(arr):
        if t == 0:
            #print(path)
            return 1
        return 0
    
    path.append('+')
    plus = fun(arr, ind+1, t-arr[ind], path)
    path.pop()
    path.append('-')
    
    minus = fun(arr, ind+1, t+arr[ind], path)
    path.pop()
    
    return plus + minus
    
    
arr = [1,2,3,1]
target = 3

out = fun(arr, ind=0, t=target)
print(out)

