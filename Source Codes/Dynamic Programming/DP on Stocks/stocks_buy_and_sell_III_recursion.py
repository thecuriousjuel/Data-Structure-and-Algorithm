def fun(arr, ind, buy, count):
    
    if count == 0 or ind == len(arr):
        return 0

    if buy == True:
        profit = max(-arr[ind] + fun(arr, ind+1, False, count),
                     0 + fun(arr, ind+1, True, count))
    else:
        profit = max(arr[ind] + fun(arr, ind+1, True, count-1),
                     0 + fun(arr, ind+1, False, count))
        
    return profit


arr = [3,3,5,0,0,3,1,4]
ind = 0
count = 2

out = fun(arr, ind, True, count)
print(out)

