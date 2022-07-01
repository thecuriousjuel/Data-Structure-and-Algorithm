def fun(day, last, points, path, dp = {}):
    
    if day == len(points)-1:
        maxi = 0

        for task in range(3):
            if task != last:
                maxi = max(maxi, points[day][task])
        
        # path.append(maxi)
        # print(path)
        # path.pop()
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]


    maxi = 0
    point = 0

    for task in range(len(points[0])):
        if task != last:
            # path.append(points[day][task])
            point = points[day][task] + fun(day+1, task, points, path, dp)
            # path.pop()
        maxi = max(maxi, point)

    dp[day][last] = maxi

    return dp[day][last]

# 8 6 4 3

points = [[2, 1, 3], 
          [7, 4, 6], 
          [5, 1, 2],
          [7, 3, 8]]

day = 0
last = 3
path = []

dp = [[-1 for _ in range(len(points[0])+1)] for _ in range(len(points)+1)] 

out = fun(day, last, points, path, dp)

# print(path)
print(out)