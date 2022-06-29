def fun(grid, row, col, path):
    
    if row == len(grid) or col == len(grid[0]):
        return 0

    if grid[row][col] == -1:
        return 0

    path.append((row, col))

    if row == len(grid)-1 and col == len(grid[0])-1:
        print('Reached Destination. Path -> ', path)
        path.pop()
        return 1 

    right = fun(grid, row, col+1, path)
    down = fun(grid, row+1, col, path)

    path.pop()

    return right + down

N = 5
M = 3

row = 0
col = 0

grid = [[0 for _ in range(M)] for _ in range(N)]
grid[1][1] = -1
grid[1][2] = -1
path = []

print(fun(grid, row, col, path))