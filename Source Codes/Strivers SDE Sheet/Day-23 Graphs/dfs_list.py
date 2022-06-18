from Graph_AdjList import g

def dfs(g, vertex, visited = []):
    visited.append(vertex)
    for i in g.graph_data[vertex]:
        if i not in visited:
            dfs(g, i, visited)
            
    if vertex == g.node_list[0]:
        return visited
            


output = dfs(g, g.node_list[0])
print(output)
