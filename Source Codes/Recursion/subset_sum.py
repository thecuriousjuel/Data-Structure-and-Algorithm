def function(arr, index=0, l = []):

    if index >= len(arr):
        return
    else:
        print(l)

    l.append(arr[index])
    function(arr, index+1, l)
    l.pop()
    function(arr, index+1, l)







s = [3,1,4]
function(s)