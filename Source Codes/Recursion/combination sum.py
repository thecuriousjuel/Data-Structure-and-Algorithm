def function(arr, target, index=0, l=[]):
 
    if index >= len(arr):
        return
    elif sum(l) >= target:
        if sum(l) == target:
            print(l)
        return

    l.append(arr[index])
    function(arr, target, index, l[:])

    l.pop()

    function(arr, target, index+1, l[:])

candidates = [2,3,6,7]
target = 7


function(candidates, target)