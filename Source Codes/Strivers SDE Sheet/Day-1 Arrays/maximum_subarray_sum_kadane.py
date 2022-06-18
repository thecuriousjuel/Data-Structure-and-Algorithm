arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = 0
max_num = arr[0]


for i in arr:
    
    max_sum += i
    
    max_num = max(max_sum, max_num)
        
    if max_sum < 0:
        max_sum = 0
        
        
print(max_num)
