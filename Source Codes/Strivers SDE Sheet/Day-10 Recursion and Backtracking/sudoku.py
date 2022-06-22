def display(matrix):
    print('-' * 20)
    for i in matrix:
        for j in i:
            print(j, end= ' ')
            
        print()
            
            
            
def is_valid(matrix, num, row, col):
    
    for i in range(9):
            
        if str(num) == matrix[row][i]:
            return False
        
        if str(num) == matrix[i][col]:
            return False
        
        if str(num) == matrix[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3]:
            return False
        
    return True
            
            
def sudoku(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == '.':
                for num in range(1, 10):
                    if is_valid(matrix, num, i, j):
                        matrix[i][j] = str(num)
                        out = sudoku(matrix)
                        if out:
                            return out
                        else:
                            matrix[i][j] = '.'
                
                return False

    
    return matrix




matrix=[['.', '5', '7', '.', '1', '3', '.', '8', '4'],
        ['4', '.', '3', '.', '5', '7', '1', '.', '6'],
        ['.', '1', '2', '.', '4', '.', '.', '3', '.'],
        ['1', '7', '.', '3', '.', '4', '.', '.', '2'],
        ['5', '.', '4', '.', '7', '.', '3', '6', '.'],
        ['.', '.', '.', '5', '.', '8', '7', '.', '1'],
        ['8', '4', '5', '7', '9', '.', '6', '1', '3'],
        ['.', '9', '1', '.', '3', '6', '.', '7', '.'],
        ['7', '.', '.', '1', '.', '5', '4', '.', '9']]


display(matrix)
out = sudoku(matrix)
display(out)



