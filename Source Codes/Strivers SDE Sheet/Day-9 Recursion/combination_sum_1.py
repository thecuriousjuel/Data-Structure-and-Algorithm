def combi_sum(arr, ans, target, index=0, out=[]):
    # print('Debug 1: ', out, index)
    
    if sum(out) == target:
        ans.append(out)
        return
    elif sum(out) > target:
        return
    
    if index == len(arr):
        return
    

    out.append(arr[index])
    combi_sum(arr, ans, target, index, out[:])
    
    index += 1
    
    out.pop()
    combi_sum(arr, ans, target, index, out[:])
    

arr = [2,3,6,7]
ans = []

combi_sum(arr, ans, target=7)

print(ans)


