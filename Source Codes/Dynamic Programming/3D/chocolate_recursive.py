def fun(grid, i, j1, j2):
    if j1 < 0 or j1 >= len(grid[0]) or j2 < 0 or j2 >= len(grid[0]):
        return float('-inf')
    
    
    if i == len(grid)-1:
        if j1 == j2:
            return grid[i][j1]
        
        else:
            return grid[i][j1] + grid[i][j2]
        
    
    maxi = float('-inf')
    for di in range(-1, 2):
        for dj in range(-1, 2):
            value = 0
            if j1 == j2:
                value = grid[i][j1]
            else:
                value = grid[i][j1] + grid[i][j2]
                
            value += fun(grid, i+1, j1+di, j2+dj)
            maxi = max(maxi, value)
            
    
    return maxi



grid = [[2, 3, 1, 2],
        [3, 4, 2, 2],
        [5, 6, 3, 5]]

i = 0
j1 = 0
j2 = len(grid[0])-1

print(fun(grid, i, j1, j2))
            