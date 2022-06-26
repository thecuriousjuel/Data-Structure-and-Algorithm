def fun(arr, n):
    prev = 0
    prev2 = 0
    curi = 0

    right = float('inf')

    for i in range(1, n):
        left = prev + abs(arr[i] - arr[i-1])
        
        if i > 1:
            right = prev2 + abs(arr[i] - arr[i-2])

        curi = min(left, right)
        
        prev2 = prev
        prev = curi

    return curi

arr = [10, 20, 30, 10, 60, 10]
n = len(arr)

print(fun(arr, n))


