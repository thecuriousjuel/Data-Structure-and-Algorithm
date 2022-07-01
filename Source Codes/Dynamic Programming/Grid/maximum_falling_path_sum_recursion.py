def fun(matrix, row, col):
    
    if row >= len(matrix) or col < 0 or col >= len(matrix):
        return float('-inf')

    # print(matrix[row][col], (row, col))

    if row == len(matrix) - 1:
        return matrix[row][col]


    left_diag = matrix[row][col] + fun(matrix, row+1, col-1)
    bottom = matrix[row][col] + fun(matrix, row+1, col)
    right_diag = matrix[row][col] + fun(matrix, row+1, col+1)

    return max(left_diag, bottom, right_diag)



matrix = [[1, 2, 10, 4], 
          [10, 3, 2, 5],
          [1, 1, 20, 2],
          [1, 2, 2, 1]]


row = 0
max_var = float('-inf')

for col in range(len(matrix[0])):
    out = fun(matrix, row, col)
    max_var = max(max_var, out)

print(max_var)