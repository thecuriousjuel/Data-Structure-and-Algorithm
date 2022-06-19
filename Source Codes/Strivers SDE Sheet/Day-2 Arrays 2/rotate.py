def rotate_clock_90(matrix):
    r = len(matrix)
    c = len(matrix[0])

    new_matrix = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[i][j] = matrix[c-j-1][i]
            
    return new_matrix


def display(m):
    for i in m:
        for j in i:
            print(j, end=' ')
        print()
    print()
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print('Input Matrix')
display(matrix)


out = rotate_clock_90(matrix)
print('Output Matrix')
display(out)

out = rotate_clock_90(out)
print('Output Matrix')
display(out)




