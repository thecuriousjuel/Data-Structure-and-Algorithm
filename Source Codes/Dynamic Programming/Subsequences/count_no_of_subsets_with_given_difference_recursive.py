def fun(arr, ind, target, path):
    if target == 0:
        print(path)
        return 1
        
    if target < 0:
        return 0
    
    if ind == len(arr):
        return 0

    path.append(arr[ind])
    pick = fun(arr, ind+1, target-arr[ind], path)
    path.pop()
    
    not_pick = fun(arr, ind+1, target, path)

    return pick + not_pick1


arr = [1, 2, 2, 3, 5, 3, 6] * 5
ind = 0
target = 6
path = []

out = fun(arr, ind, target, path)
print(out)

        

