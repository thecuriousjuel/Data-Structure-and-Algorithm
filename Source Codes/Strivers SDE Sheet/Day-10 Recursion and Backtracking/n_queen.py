def display(matrix):
    print('-'*20)
    
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

        

def is_valid(matrix, n, row, col):

    # Left side

    i = col - 1
    
    while i >= 0:
        if matrix[row][i] == 'Q':
            return False
        
        i -= 1
        
    i = row - 1
    j = col - 1

    # Top left diagonal

    while i >= 0 and j >= 0:
        if matrix[i][j] == 'Q':
            return False
        
        i -= 1
        j -= 1
        
        
    i = row + 1
    j = col - 1

    # Bottom right diagonal
    
    while i < n and j >= 0:
        if matrix[i][j] == 'Q':
            return False
    
        i += 1
        j -= 1
    

    return True


def fun(matrix, n, col, out):
    if col == n:
        t1 = []
        for i in matrix:
            t1.append(i[:])

        out.append(t1)
        return
    
    for i in range(n):
        if is_valid(matrix, n, i, col):
            matrix[i][col] = 'Q'
            fun(matrix, n, col+1, out)
            matrix[i][col] = '.'


n = int(input('Enter a value -> '))
matrix = [['.' for _ in range(n)] for _ in range(n)]

# display(matrix)

col = 0
out = []

fun(matrix, n, col, out)

for i in out:
    display(i)








