def fun(arr, n, k):
    if n == 0:
        return 0

    min_energy = float('inf')
    for i in range(1, k+1):
        if n-i >=0:
            out = fun(arr, n-i, k) + abs(arr[n] - arr[n-i])
            min_energy = min(min_energy, out)
    
    return min_energy
    
    
arr = [30, 10, 60, 10, 60, 50]
n = len(arr)
print(fun(arr, n-1, k=3))
