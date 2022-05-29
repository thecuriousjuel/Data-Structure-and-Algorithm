def function(arr, index=0, l = []):
    if index >= len(arr):
        print(l)
        return

    l.append(arr[index])
    function(arr, index+1, l[:])
    l.pop()
    function(arr, index+1, l[:])


function([3,2,1,5])