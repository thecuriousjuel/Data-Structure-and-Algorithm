"""
    Program to find out the number of unique paths in a grid
    
"""

def fun(maze, row, col, path, ans):
    
    if row == len(maze):
        return
    
    if col == len(maze[0]):
        return

    path.append((row, col))
    
    if row == len(maze)-1 and col == len(maze[0])-1:
        print('Destination reached. Path -> ', path)
        ans[0] += 1
    
    fun(maze, row, col+1, path, ans)
    fun(maze, row+1, col, path, ans)
    path.pop()


N = 4
M = 4
row, col = 0, 0
ans = [0]
path = []

maze = [[1 for _ in range(M)] for _ in range(N)]

fun(maze, row, col, path, ans)
print(ans[0])
