def fun(arr, ind, k):
    # print(ind, k)
    if k == 0:
        return 1
    
    if ind >= len(arr):
        return 0
    
    pick = 0
    if k >= arr[ind]:
        pick = fun(arr, ind+1, k-arr[ind])
        
    not_pick = fun(arr, ind+1, k)
    
    return pick + not_pick
    

arr = [1,2,2,3]

out = fun(arr, ind=0, k=3)

print(out)
