def fun(arr, task, day, last, dp):
    
    # print(f'Day={day}, Last={last}')
    
    if day == 0:
        maxi = float('-inf')
        
        for i in range(task):
            if i != last:
                maxi = max(maxi, arr[day][i])
        
        return maxi
    
    if dp[day][task] != -1:
        return dp[day][task]
    
    maxi = float('-inf')
    for i in range(task):
        if i != last:
            s = arr[day][i] + fun(arr, task, day-1, i, dp)
            maxi = max(maxi, s)
            
    dp[day][task] = maxi
    return dp[day][task]


#arr = [[1,2,5],[3,4,1],[4,3,3]]
arr = [[10, 50, 1], [5, 100, 11]]

task = len(arr[0])
day = len(arr)-1

dp = [[-1 for _ in range(len(arr[0])+1)] for _ in range(len(arr)+1)]

out = fun(arr, task, day, -1, dp)
print(out)



