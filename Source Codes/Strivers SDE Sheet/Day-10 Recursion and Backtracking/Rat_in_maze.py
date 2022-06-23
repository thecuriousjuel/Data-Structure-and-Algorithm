def rat_in_maze(matrix, visited, ans, row=0, col=0, path=[]):

    row_size = len(matrix)
    col_size = len(matrix[0])
    
    if row == row_size-1 and col == col_size-1:
        ans.append(path[:])
        return

    # right side
    if col + 1 < col_size and matrix[row][col+1] == 1 and visited[row][col+1] == False:
        
        visited[row][col] = True
        path.append('R')
        rat_in_maze(matrix, visited, ans, row, col+1, path)
        visited[row][col] = False
        path.pop()
        
    # left side
    if col - 1 >= 0 and matrix[row][col-1] == 1 and visited[row][col-1] == False:
        
        visited[row][col] = True
        path.append('L')
        rat_in_maze(matrix, visited, ans, row, col-1, path)
        visited[row][col] = False
        path.pop()
        
    # Bottom Side
    if row + 1 < row_size and matrix[row+1][col] == 1 and visited[row+1][col] == False:
        
        visited[row][col] = True
        path.append('D')
        rat_in_maze(matrix, visited, ans, row+1, col, path)
        visited[row][col] = False
        path.pop()
        
    # Top Side
    if row - 1 >= 0 and matrix[row-1][col] == 1 and visited[row-1][col] == False:
        
        visited[row][col] = True
        path.append('T')
        rat_in_maze(matrix, visited, ans, row-1, col, path)
        visited[row][col] = False
        path.pop()
            
 
 
R = 5
C = 5

visited = [[False for _ in range(C)] for _ in range(R)]

matrix = [[1,0,1,1,1],
          [1,0,1,0,1],
          [1,1,1,0,1],
          [0,1,1,1,1]]

ans = []

rat_in_maze(matrix, visited, ans)
print(ans)
