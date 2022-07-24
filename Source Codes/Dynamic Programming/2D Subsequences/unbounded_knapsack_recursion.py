def fun(wt, val, ind, W):
    if W == 0:
        return 0
    
    if ind == len(wt):
        return float('-inf')
    
    
    pick = float('-inf')
    if W-wt[ind] >= 0:
        pick = val[ind] + fun(wt, val, ind, W-wt[ind])

    not_pick = 0 + fun(wt, val, ind+1, W)
    
    return max(pick, not_pick)


wt = [1, 3, 4, 5]
val = [10, 40, 50, 70]
W = 8

out = fun(wt, val, ind=0, W=W)
print(out)


