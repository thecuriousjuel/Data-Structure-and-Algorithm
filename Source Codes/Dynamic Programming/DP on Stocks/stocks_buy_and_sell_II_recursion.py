# Buy and Sell infinite times

def fun(arr, ind, buy):
    if ind == len(arr):
        return 0


    if buy == True:
        profit = max(-arr[ind] + fun(arr, ind+1, False), 0 + fun(arr, ind+1, True))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, True), 0 + fun(arr, ind+1, False))
        
    return profit


arr = [7,1,5,3,6,4]
ind = 0

out = fun(arr, ind, True)
print(out)
