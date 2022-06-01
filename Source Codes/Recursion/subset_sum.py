ans = []

def function(arr, index=0, l = []):
    global ans

    if index >= len(arr):
        # print(l, sum(l))
        ans.append(sum(l))
        return 


    l.append(arr[index])
    function(arr, index+1, l[:])
        
    l.pop()

    function(arr, index+1, l[:])



s = [3,1,2]
function(s)
print(ans)