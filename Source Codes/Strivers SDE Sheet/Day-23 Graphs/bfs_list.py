from Graph_AdjList import g

def bfs(g, vertex):
    queue = [vertex]
    visited = [vertex]
    
    while len(queue) > 0:
        start = queue[0]
        
        for i in g.graph_data[start]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
        
        queue = queue[1:]
        
    return visited


output = bfs(g, g.node_list[0])
print('BFS : ', output)