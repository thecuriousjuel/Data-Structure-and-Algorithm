def fun(nums, index, ans_list, target, ds=[]):
    if sum(ds) == target:
        ans_list.append(ds)
        
    for i in range(index, len(nums)):
        if i != index and nums[i] == nums[i-1]:
            continue
        
        ds.append(nums[i])
        fun(nums, i+1, ans_list, target, ds[:])
        
        ds.pop()
        
    if index == 0:
        return ans_list
        
        
nums = [10,1,2,7,6,1,5]
nums.sort()
ans_list = []
index = 0
target = 8

out = fun(nums, index, ans_list, target)
print(out)



# def combi_sum(arr, ans, target, index=0, out=[]):
    
#     if index == len(arr):
#         if sum(out) == target:
#             ans.append(out)
#         return
    
    
#     out.append(arr[index])
#     combi_sum(arr, ans, target, index+1, out[:])
    
#     out.pop()
#     combi_sum(arr, ans, target, index+1, out[:])


# arr = [10,1,2,7,6,1,5]
# target = 8

# ans = []

# combi_sum(sorted(arr), ans, target)
# print(ans)
