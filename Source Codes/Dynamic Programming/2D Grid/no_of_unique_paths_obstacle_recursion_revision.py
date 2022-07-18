def fun(arr, row, col):
    
    if col == len(arr[0]):
        return 0
    
    if row == len(arr):
        return 0
    
    if arr[row][col] == -1:
        return 0
    
    if row == len(arr)-1 and col == len(arr[0])-1:
        return 1
    
    right = fun(arr, row, col+1)
    down = fun(arr, row+1, col)
    
    return right + down


n = 3

arr = [[1 for _ in range(n)] for _ in range(n)]
arr[0][2] = -1
#print(arr)

out = fun(arr, row=0, col=0)

print(out)




