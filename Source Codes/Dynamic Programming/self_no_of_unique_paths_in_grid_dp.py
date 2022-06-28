"""
    Program to find out the number of unique paths in a grid using Dynamic Programming
    
"""

def fun(maze, row, col, path, dp):

    if row == len(maze) or col == len(maze[0]):
        return 0

    path.append((row, col))
    # print(dp, (row, col))
    
    if row == len(maze)-1 and col == len(maze[0])-1:
        # print('Destination reached. Path -> ', path)

        path.pop()
        return 1

    if dp[row][col] != 0:
        return dp[row][col]

    left = fun(maze, row, col+1, path, dp)

    right = fun(maze, row+1, col, path, dp)
    path.pop()

    dp[row][col] = left + right

    return dp[row][col]


N = 3
M = 3
row, col = 0, 0
path = []

maze = [[1 for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]

fun(maze, row, col, path, dp)
# print(dp)
print(dp[0][0])

