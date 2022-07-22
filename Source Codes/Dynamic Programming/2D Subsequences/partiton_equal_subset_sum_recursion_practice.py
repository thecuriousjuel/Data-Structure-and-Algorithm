def fun(arr, ind, k):    
    if k == 0:
        return True
    
    if ind >= len(arr)-1:
        return False

    pick = False
    if k-arr[ind] >= 0:
        pick = fun(arr, ind+1, k-arr[ind])
        if pick == True:
            return True
    
    not_pick = fun(arr, ind+1, k)
    if not_pick == True:
        return True
    
    return pick or not_pick


arr = [2,8,6]
s = 0
ind = 0

for i in arr:
    s += i
    
if s % 2 == 0:
    out = fun(arr, ind, k=s//2)
else:
    out = False
    
print(out)

