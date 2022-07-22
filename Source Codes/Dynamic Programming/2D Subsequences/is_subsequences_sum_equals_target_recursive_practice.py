def fun(arr, ind, path, target):
    if target == 0:
        print(path)
        return True
    
    if target < 0:
        return False
    
    if ind == len(arr)-1:
        return arr[ind] == target

    
    path.append(arr[ind])
    left = fun(arr, ind+1, path, target-arr[ind])
    if left:
        return left

    path.pop()
    
    right = fun(arr, ind+1, path, target)
    if right:
        return right

    return left or right


arr = [2, 3, 3, 3, 4, 5]
ind = 0
path = []
target = 11

print(fun(arr, ind, path, target))

