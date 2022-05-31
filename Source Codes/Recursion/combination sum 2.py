def function(arr, target, index=0, l=[]):
 
    if index >= len(arr):
        return
    elif sum(l) >= target:
        if sum(l) == target:
            print(l)
        return

    l.append(arr[index])
    function(arr, target, index+1, l[:])

    l.pop()

    function(arr, target, index+1, l[:])

candidates = [2,1,1,2]
target = 4


function(sorted(candidates), target)