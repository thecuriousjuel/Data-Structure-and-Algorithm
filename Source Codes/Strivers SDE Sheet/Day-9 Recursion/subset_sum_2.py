def fun(index, nums, ds=[], ans_list=[]):
    ans_list.append(ds)
    
    #  print(ds, end=' ')
    
    for i in range(index, len(nums)):
        if i != index and nums[i] == nums[i-1]:
            continue
        
        ds.append(nums[i])
        fun(i+1, nums, ds[:], ans_list)
        
        ds.pop()
        
        
    if index == 0:
        return ans_list
        
        
nums = [1,2,2,3]
nums.sort()

out = fun(index=0, nums=nums)
print(out)

    
    
