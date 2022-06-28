"""
    Program to find out the number of unique paths in a grid
    
"""

def fun(maze, row, col, path):
    
    if row == len(maze) or col == len(maze[0]):
        return 0

    path.append((row, col))
    
    if row == len(maze)-1 and col == len(maze[0])-1:
        # print('Destination Reached. Path -> ', path)
        path.pop()
        return 1
    
    right = fun(maze, row, col+1, path)
    down = fun(maze, row+1, col, path)
    path.pop()

    return right + down


N = 15
M = 15
row, col = 0, 0
path = []

maze = [[1 for _ in range(M)] for _ in range(N)]

out = fun(maze, row, col, path)
print(out)
