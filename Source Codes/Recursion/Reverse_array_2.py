def function(arr, l, r):
    if l >= r:
        return arr

    arr[l], arr[r] = arr[r], arr[l]
    return function(arr, l+1, r-1)
    


arr = [1, 4, 5, 8, 9]
n = len(arr)
print(function(arr, 0, n-1))
