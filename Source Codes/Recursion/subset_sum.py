def function(arr, index=0, l = [], ans = []):

    if index >= len(arr):
        print(l, sum(l))
        return sum(l)


    l.append(arr[index])
    t = function(arr, index+1, l[:])
    if t:
        ans.append(t)
        
    l.pop()

    t = function(arr, index+1, l[:])
    if t:
        ans.append(t)




s = [3,1,2]
print(function(s))
