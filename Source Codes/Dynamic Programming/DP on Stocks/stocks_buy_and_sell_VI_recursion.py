def fun(arr, ind, buy, fee):
    
    if ind == len(arr):
        return 0
    
    if buy == 1:
        profit = max(-arr[ind] + fun(arr, ind+1, 0, fee),
                     0 + fun(arr, ind+1, 1, fee))
    else:
        profit = max(-fee + arr[ind] + fun(arr, ind+1, 1, fee),
                     0 + fun(arr, ind+1, buy, fee))
        
    return profit


price = [4,9,0,4,10]
ind = 0
buy = 1
fee = 2

out = fun(price, ind, buy, fee)
print(out)

