def fun(arr, ind, k):
    # print(k)
    if k == 0:
        return True
    
    if ind == len(arr)-1:
        return False
    
    pick = False
    if k >= arr[ind]:
        pick = fun(arr, ind+1, k-arr[ind])
        if pick:
            return pick
        
    not_pick = fun(arr, ind+1, k)
    if not_pick:
        return not_pick
    
    return pick or not_pick


arr = [1,2,3,4]
k = 8

out = fun(arr, ind=0, k=k)

print(out)

