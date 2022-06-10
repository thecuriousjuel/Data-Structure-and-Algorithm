from Graph import g


def dfs(graph, start, vertex_list, visited, output = []):
    start_index = vertex_list.index(start)
    output.append(start)
    # print(start, end=' ')
    visited[start_index] = 1

    for i in range(len(graph[start_index])):
        if graph[start_index][i] == 1 and visited[i] == 0:
            dfs(graph, vertex_list[i], vertex_list, visited, output)

        
    if start == g.vertex_list[0]:
        return output
     

print(dfs(g.graph, g.vertex_list[0], g.vertex_list, g.visited))