def fun(day, last, points):
    
    if day == len(points)-1:
        maxi = 0

        for task in range(len(points[0])):
            if task != last:
                maxi = max(maxi, points[day][task])
        
        return maxi

    maxi = 0
    point = 0

    for task in range(len(points[0])):
        if task != last:
            point = points[day][task] + fun(day+1, task, points)
        maxi = max(maxi, point)

    return maxi

# 8 6 4 3

"""
points = [[2, 1, 3], 
          [7, 4, 6], 
          [5, 1, 2],
          [7, 3, 8]]
"""

points = [[10, 50, 1], 
          [5, 100, 11]]


day = 0
last = len(points[0])

out = fun(day, last, points)

print(out)