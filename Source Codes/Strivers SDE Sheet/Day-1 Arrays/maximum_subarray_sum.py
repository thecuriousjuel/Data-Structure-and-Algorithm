arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = arr[0]


for i in range(len(arr)):
    for j in range(len(arr)):
        cal = 0
        for k in range(i, j+1):
            cal += arr[k]
            
        max_sum = max(cal, max_sum)
        
        
print(max_sum)
    

