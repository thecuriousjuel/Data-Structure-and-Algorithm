def fun(arr, task, day, last):
    
    print(f'Day={day}, Last={last}')
    
    if day == 0:
        maxi = float('-inf')
        
        for i in range(task):
            if i != last:
                maxi = max(maxi, arr[day][i])
        
        return maxi
                
    
    maxi = float('-inf')
    for i in range(task):
        if i != last:
            s = arr[day][i] + fun(arr, task, day-1, i)
            maxi = max(maxi, s)
            
    return maxi


arr = [[1,2,5],[3,4,1],[4,3,3]]

task = len(arr[0])
day = len(arr)-1

out = fun(arr, task, day, -1)
print(out)



