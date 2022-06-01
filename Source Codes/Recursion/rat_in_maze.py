def solve(maze, visited, start_row=0, start_col=0, sol=''):

    print(start_row, start_col)

    if start_row == len(maze)-1 and start_col == len(maze)-1:
        print('Reached Solution : ', sol)
        return

    # To go downward direction
    if start_row+1 < len(maze) and visited[start_row+1][start_col] == 0 and maze[start_row+1][start_col] == 1:
        visited[start_row][start_col] = 1
        solve(maze, visited[:][:], start_row+1, start_col, sol + 'D')
        visited[start_row][start_col] = 0

    # To go in left direction
    if start_col-1 >= 0 and visited[start_row][start_col-1] == 0 and maze[start_row][start_col-1] == 1:
        visited[start_row][start_col] = 1
        solve(maze, visited[:][:], start_row, start_col-1, sol + 'L')
        visited[start_row][start_col] = 0

    # To go in right direction
    if start_col+1 < len(maze) and visited[start_row][start_col+1] == 0 and maze[start_row][start_col+1] == 1:
        visited[start_row][start_col] = 1
        solve(maze, visited[:][:], start_row, start_col+1, sol + 'R')
        visited[start_row][start_col] = 0

    # To go in upward direction
    if start_row-1 >= 0 and visited[start_row-1][start_col] == 0 and maze[start_row-1][start_col] == 1:
        visited[start_row][start_col] = 1
        solve(maze, visited[:][:], start_row-1, start_col, sol + 'U')
        visited[start_row][start_col] = 0


maze = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]

# maze = [
#     [1, 1, 1, 1],
#     [1, 1, 0, 1],
#     [1, 0, 1, 1],
#     [1, 1, 1, 1]
# ]

visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]

solve(maze, visited)
