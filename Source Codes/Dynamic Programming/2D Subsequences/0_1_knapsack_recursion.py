def fun(ind, wt, W, val):
    if ind == len(wt)-1:
        if W >= wt[ind]:
            return val[ind]
        else:
            return 0

    pick = float('-inf')
    if W-wt[ind] >=0:
        pick = val[ind] + fun(ind+1, wt, W-wt[ind], val)
        
    not_pick = 0 + fun(ind+1, wt, W, val)
    
    return max(pick, not_pick)


W = 50
wt = [10, 20, 30]
val = [60, 100, 120]

out = fun(ind=0, wt=wt, W=W, val=val)
print(out)

