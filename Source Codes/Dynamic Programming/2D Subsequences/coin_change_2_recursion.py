def fun(arr, ind, t, path=[]):
    
    if t == 0:
        print(path)
        return 1
    
    if ind == len(arr):
        return 0
    
        
    pick = 0
    if t-arr[ind] >= 0:
        path.append(arr[ind])
        pick = fun(arr, ind, t-arr[ind])
        path.pop()
        
    not_pick = fun(arr, ind+1, t)
    
    return pick + not_pick


arr = [1,2,3]
t = 4

out = fun(arr, ind=0, t=t)
print(out)

