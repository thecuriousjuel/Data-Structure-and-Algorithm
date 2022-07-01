def fun(arr, ind, path, target):
    
    if target == 0:
        print(path)
        return True
    
    if target < 0:
        return False
    
    if ind == len(arr):
        return False
    
    
    path.append(arr[ind])
    left = fun(arr, ind+1, path, target-arr[ind])
    path.pop()
    
    right = fun(arr, ind+1, path, target)

    return left or right


arr = [1, 2, 3, 4, 8]
ind = 0
path = []
target = 15

print(fun(arr, ind, path, target))

