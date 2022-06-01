def solve(maze, visited, di, dj, start_row=0, start_col=0, sol=''):

    print(start_row, start_col)

    if start_row == len(maze)-1 and start_col == len(maze)-1:
        print('Reached Solution : ', sol)
        return

    dir = 'DLRU'
    for ind in range(len(di)):

        nexti = start_row + di[ind]
        nextj = start_col + dj[ind]

        if nexti >= 0 and nexti < len(maze) and nextj >= 0 and nextj < len(maze) and visited[nexti][nextj] == 0 and maze[nexti][nextj]:
            visited[start_row][start_col] = 1
            solve(maze, visited, di, dj, nexti, nextj, sol + dir[ind])
            visited[start_row][start_col] = 0


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1]
]

# maze = [
#     [1, 1, 1, 1],
#     [1, 1, 0, 1],
#     [1, 0, 1, 1],
#     [1, 1, 1, 1]
# ]


di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]

visited = [[0 for _ in range(len(maze))] for _ in range(len(maze))]

solve(maze, visited, di, dj)
