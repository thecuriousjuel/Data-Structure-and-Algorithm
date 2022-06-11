from Graph import g

def bfs(graph, start, vertex_list, visited, output=[]):
    queue = [start]
    output = [start]

    visited[vertex_list.index(start)] = 1

    while len(queue) > 0:
        t = queue[0]
        t_index = vertex_list.index(t)

        for i in range(len(graph[t_index])):
            if graph[t_index][i] == 1 and visited[i] == 0:
                queue.append(vertex_list[i])
                output.append(vertex_list[i])
                visited[i] = 1

        queue = queue[1:]

    return output

print(bfs(g.graph, g.vertex_list[0], g.vertex_list, g.visited))
