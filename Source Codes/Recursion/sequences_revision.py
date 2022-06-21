def seq(arr, index=0, out=[], ans = []):
    
    if index == len(arr):
        ans.append(out)
        return
    
    seq(arr, index+1, out[:], ans)
    out.append(arr[index])
    
    seq(arr, index+1, out[:], ans)
    out.pop()
    
    if index == 0:
        return ans
    

arr = [3,4,1]

print(seq(arr))