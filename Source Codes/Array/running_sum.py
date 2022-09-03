nums = [1,1,1,1,1]

temp = [nums[0]]

for i in range(1, len(nums)):
    temp.append(temp[i-1] + nums[i])
    
print(temp)