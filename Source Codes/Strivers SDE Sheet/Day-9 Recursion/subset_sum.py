def subset_sum(arr, index=0, out = [], sub_sum = []):
    
    if index == len(arr):
        sub_sum.append(sum(out))
        return    
    
    out.append(arr[index])
    subset_sum(arr, index+1, out[:], sub_sum)
    
    out.pop()
    subset_sum(arr, index+1, out[:], sub_sum)
    
    if index == 0:
        return sub_sum
    
    
    
    
arr = [5,2,1]

out = subset_sum(arr)
print(sorted(out))
    

