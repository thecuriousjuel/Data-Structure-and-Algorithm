def fun(arr, ind, buy):
    if ind == len(arr):
        return 0


    if buy == False:
        profit = max(-arr[ind] + fun(arr, ind+1, True), 0 + fun(arr, ind+1, False))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, False), 0 + fun(arr, ind+1, True))
        
    return profit


arr = [7,1,5,3,6,4]
ind = 0

out = fun(arr, ind, False)
print(out)
