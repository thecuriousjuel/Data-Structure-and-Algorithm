def function(arr, index=0, l = [], ans = []):

    if index >= len(arr):
        print(l, sum(l))
        return sum(l)


    l.append(arr[index])
    t = function(arr, index+1, l[:])
        
    l.pop()

    t = function(arr, index+1, l[:])


s = [3,1,2]
print(function(s))
