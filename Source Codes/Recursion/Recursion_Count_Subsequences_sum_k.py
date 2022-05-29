def function(arr, K, index = 0, l = []):
    if index >= len(arr):
        if sum(l) == K:
            print(l)
            return 1
        return 0

    l.append(arr[index])

    left = function(arr, K, index+1, l[:])
    l.pop()
    right = function(arr, K, index+1, l[:])

    return left + right


arr = [1,2,1]
K = 2

print(function(arr, K))