def fun(arr, ind, k):
    if ind == 0:
        return 0
    
    min_value = float('inf')
    
    for i in range(1, k+1):
        if ind - i >= 0:
            steps = fun(arr, ind-i, k) + abs(arr[ind] - arr[ind - i])

        min_value = min(min_value, steps)

    return min_value


arr = [10, 20, 30, 10, 50, 30]
ind = len(arr)-1
k = 3

out = fun(arr, ind, k)
print(out)
    
