def function(arr, K, index=0, l = []):
    if index >= len(arr):
        if sum(l) == K:
            print(l)
            return True
        return

    l.append(arr[index])
    if function(arr, K, index+1, l[:]) == True:
        return True
        
    l.pop()

    if function(arr, K, index+1, l[:]) == True:
        return True

    return False

print(function([1,2,1], K=5))
