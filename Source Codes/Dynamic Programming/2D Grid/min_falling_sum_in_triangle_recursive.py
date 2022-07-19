def fun(tri, row, col):
    
    if row == len(tri) - 1:
        return tri[row][col]
    
    down = tri[row][col] + fun(tri, row+1, col)
    right_diag = tri[row][col] + fun(tri, row+1, col+1)
    
    return min(down, right_diag)


tri = [[1],
       [2, 3],
       [3, 6, 7],
       [8, 9, 6, 10]]


print('Final : ', fun(tri, row=0, col=0))