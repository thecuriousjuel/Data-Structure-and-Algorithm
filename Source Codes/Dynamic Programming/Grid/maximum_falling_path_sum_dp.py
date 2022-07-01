def fun(matrix, row, col, dp):
    
    if row >= len(matrix) or col < 0 or col >= len(matrix):
        return float('-inf')

    # print(matrix[row][col], (row, col))

    if row == len(matrix) - 1:
        return matrix[row][col]

    if dp[row][col] != -1:
        return dp[row][col]

    left_diag = matrix[row][col] + fun(matrix, row+1, col-1, dp)
    bottom = matrix[row][col] + fun(matrix, row+1, col, dp)
    right_diag = matrix[row][col] + fun(matrix, row+1, col+1, dp)

    dp[row][col] = max(left_diag, bottom, right_diag)

    return dp[row][col]


matrix = [[1, 2, 10, 4], 
          [100, 3, 2, 5],
          [1, 1, 20, 2],
          [1, 2, 2, 1]]


row = 0
max_var = float('-inf')
dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

for col in range(len(matrix[0])):
    out = fun(matrix, row, col, dp)
    max_var = max(max_var, out)

    dp[0][col] = max_var

print(max_var)