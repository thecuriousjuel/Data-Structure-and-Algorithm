def fun(arr, ind, t):
    #print(ind, t)
    
    if ind == len(arr)-1:
        if t % arr[ind] == 0:
            return t // arr[ind]
        return float('inf')

    pick = float('inf')
    if t-arr[ind] >= 0:
        pick = 1 + fun(arr, ind, t-arr[ind])
        
    not_pick = 0 + fun(arr, ind+1, t)
    
    return min(pick, not_pick) 
    

arr = [1,2,3]
t = 8

out = fun(arr, ind=0, t=t)
print(out)




