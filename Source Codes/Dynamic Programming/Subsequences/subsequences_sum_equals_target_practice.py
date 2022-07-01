def fun(arr, ind, path, target):
    # print(ind, path, target)
    
    if target == 0:
        print('Path Taken : ', path)
        return
    
    if target < 0:
        return
    
    if ind == len(arr):
        return
    
    
    path.append(arr[ind])
    fun(arr, ind+1, path, target-arr[ind])
    path.pop()
    
    fun(arr, ind+1, path, target)


arr = [1, 2, 3, 4, 8]
ind = 0
path = []
target = 10

fun(arr, ind, path, target)

