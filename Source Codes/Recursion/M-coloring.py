def function(matrix, m, start, colored, visited, n):
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and visited[i] == 0:
            visited[i] = 1
            for j in range(len(m)):
                if colored[i] == m[j]:
                    continue
                
                temp = colored[i]
                colored[i] = m[j]
                function(matrix, m, i, colored[:])
                colored[i] = temp

    visited[i] = 0



matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 0]
]

m = 'RGB'

start = 0
colored = [-1 for _ in range(len(matrix))]
colored[start] = 'R'

visited = [0 for _ in range(len(matrix))]
visited[start] = 1

print(matrix, m, start, colored, visited, n=0)