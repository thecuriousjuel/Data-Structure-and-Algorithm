def fun(arr, row, col):
    if row == len(arr) or col == len(arr[0]):
        return float('inf')
    
    if row == len(arr)-1 and col == len(arr[0])-1:
        return arr[row][col]


    left = arr[row][col] + fun(arr, row, col+1)
    down = arr[row][col] + fun(arr, row+1, col)
    
    return min(left, down)


arr = [[5,9,6],
       [11,5,2]]


out = fun(arr, row=0, col=0)
print(out)


