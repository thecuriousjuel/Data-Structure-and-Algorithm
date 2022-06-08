def triplet(arr, index=0, l=[], out=[]):
    if index >= len(arr):
        if sum(l) == 0:
            out.append(l)
        return

    l.append(arr[index])
    triplet(arr, index+1, l[:], out)
    l.pop()
    triplet(arr, index+1, l[:], out)

    if index == 0:
        print(out)
        

arr = [-1,0,1,2,-1,-4]
triplet(arr)