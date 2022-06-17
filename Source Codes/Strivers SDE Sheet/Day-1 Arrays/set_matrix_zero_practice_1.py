def display(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = '\t')
            
        print()




# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

print('-'*20)
print('Before')
print('-'*20)
print(display(matrix))
print('-'*20)

zeros = []

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] == 0:
            zeros.append((row, col))
            
            
for row, col in zeros:
    for i in range(len(matrix[row])):
        matrix[row][i] = 0
        
    for i in range(len(matrix)):
        matrix[i][col] = 0
        
print('-'*20)
print('After')
print('-'*20)
print(display(matrix))
print('-'*20)