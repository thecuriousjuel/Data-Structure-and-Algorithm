# Buy and Sell infinite times but with cooldown

def fun(arr, ind, buy):
    
    if ind >= len(arr):
        return 0
    
    if buy == 1:
        profit = max(-arr[ind] + fun(arr, ind+1, buy=0),
                     0 + fun(arr, ind+1, buy=1))
    else:
        profit = max(arr[ind] + fun(arr, ind+2, buy=1),
                     0 + fun(arr, ind+1, buy=0))
        
    return profit


price = [4,9,0,4,10]
ind = 0
buy = 1

out = fun(price, ind, buy)
print(out)
