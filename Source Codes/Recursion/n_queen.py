def is_safe(row, col, board, n):

    temp_row = row
    temp_col = col

    while row >= 0 and col >= 0:
        if board[row][col] == 'Q':
            return False
        
        row -= 1
        col -= 1


    row = temp_row
    col = temp_col

    while col >= 0:
        if board[row][col] == 'Q':
            return False

        col -= 1

    row = temp_row
    col = temp_col

    while row < n and col >= 0:
        if board[row][col] == 'Q':
            return False

        row += 1
        col -= 1

    return True



def solve(col, board, n):
    if col == n:
        print('-' * 50)
        for i in board:
            for j in i:
                print(j, end='\t')
            print()

        return


    for row in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 'Q'
            solve(col+1, board, n)
            board[row][col] = '.'
        


n = 4
board = [['.' for _ in range(n)] for _ in range(n)]
solve(col = 0, board=board, n=n)
