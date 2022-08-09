# Buy and Sell at max 'k' transaction

def fun(arr, ind, buy, k):
    
    if ind == len(arr):
        return 0
    
    if k == 0:
        return 0    
    
    # Can buy
    if buy == 1:
        profit = max(-arr[ind] + fun(arr, ind+1, 0, k), 0 + fun(arr, ind+1, 1, k))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, 1, k-1), 0 + fun(arr, ind+1, 0, k))
        
    return profit


arr = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]

out = fun(arr, ind=0, buy=1, k=7)

print(out)


