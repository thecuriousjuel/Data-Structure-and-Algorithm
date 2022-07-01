def fun(arr, n):
    if n == 0:
        return 0
    
    left = fun(arr, n-1) + abs(arr[n] - arr[n-1])
    right = float('inf')
    
    if n > 1:
        right = fun(arr, n-2) + abs(arr[n] - arr[n-2])

    return min(left, right)


arr = [10, 20, 30, 10, 60, 10]
n = len(arr)

print(fun(arr, n-1))


