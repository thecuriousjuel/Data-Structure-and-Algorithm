def fun(arr, ind, path, target):
    if target == 0:
        # print(path)
        return True
    
    if target < 0:
        return False
    
    if ind == len(arr):
        return

    
    path.append(arr[ind])
    left = fun(arr, ind+1, path, target-arr[ind])

    path.pop()
    
    right = fun(arr, ind+1, path, target)

    return left or right


arr = [2, 3, 3, 3, 4, 5]
ind = 0
path = []

s = sum(arr)
if s % 2 != 0:
    print('False')
else:
    target = s // 2
    print(fun(arr, ind, path, target))

