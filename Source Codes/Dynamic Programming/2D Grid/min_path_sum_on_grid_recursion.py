def fun(matrix, row, col):

    if row == len(matrix) or col == len(matrix[0]):
        return float('inf')

    if row == len(matrix)-1 and col == len(matrix[0]) - 1:
        return matrix[row][col]

    right = matrix[row][col] + fun(matrix, row, col+1)
    down = matrix[row][col] + fun(matrix, row+1, col)

    return min(right, down)


matrix = [[10, 8, 2], [10, 5, 100], [1, 1, 2]]
row = 0
col = 0

print(fun(matrix, row, col))

