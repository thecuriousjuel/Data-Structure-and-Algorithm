def display(arr):
    for i in arr:
        for j in i:
            print(j, end = '\t')
        print()

arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# arr = [ [1,1,1],
#         [1,0,1],
#         [1,1,0]]

print('Input Matrix')
display(arr)

n_rows = len(arr)
n_cols = len(arr[0])

pos_zero_row = []
pos_zero_col = []

for i in range(n_rows):
    for j in range(n_cols):
        if arr[i][j] == 0:
            pos_zero_row.append(i)
            pos_zero_col.append(j)


for i in range(len(pos_zero_row)):
    for j in range(n_rows):
        arr[j][pos_zero_col[i]] = 0

    for j in range(n_cols):
        arr[pos_zero_row[i]][j] = 0

print('Changed Matrix')
display(arr)