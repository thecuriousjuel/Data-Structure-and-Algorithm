def function(arr, K, index=0, l = [], ):
    if index >= len(arr):
        if sum(l) == K:
            print(l)
        return

    l.append(arr[index])
    function(arr, K, index+1, l[:])
    l.pop()
    function(arr, K, index+1, l[:])

function([1,2,1], K=3)
