def fun(matrix, row, col, dp):

    if row == len(matrix) or col == len(matrix[0]):
        return float('inf')

    if row == len(matrix)-1 and col == len(matrix[0]) - 1:
        return matrix[row][col]

    if dp[row][col] != 0:
        return dp[row][col]

    right = matrix[row][col] + fun(matrix, row, col+1, dp)
    down = matrix[row][col] + fun(matrix, row+1, col, dp)

    path.pop()

    dp[row][col] = min(right, down)

    return dp[row][col]


matrix = [[10, 8, 2], [10, 5, 100], [1, 1, 2]]
row = 0
col = 0
path = []
dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

print(fun(matrix, row, col, path, dp))

