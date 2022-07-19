def fun(arr, row, col):
    
    if row == len(arr)-1:
        return arr[row][col]

    down = arr[row][col] + fun(arr, row+1, col)
    right_diag = arr[row][col] + fun(arr, row+1, col+1)

    return min(down, right_diag)


arr = [[1],
       [2,3],
       [3,6,7],
       [8,9,6,10]]

out = fun(arr, row=0, col=0)

print(out)