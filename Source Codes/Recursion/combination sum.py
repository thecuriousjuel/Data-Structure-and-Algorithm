def function(arr, target, index=0, l=[]):
    if index >= len(arr):
        if sum(l) == target:
            return l
        return 

    t = function(arr, target, index+1, l[:])
    if t != None:
        return t
    l.append(arr[index])
    t = function(arr, target, index+1, l[:])
    if t != None:
        return t


candidates = [2,3,6,7]
target = 7


print(function(candidates, target))