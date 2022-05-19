from Graph_Adjacency_Matrix import Graph

def dfs_helper(current_node):


# g.node_data


def dfs(root):
    # case 1: If there is a dead end
    # case 2: If the node is already visited
    # case 3: If there are many unvisited nodes
    # case 4: If there are many visited nodes

    for node in range(len(root)):
        for current in range(len(node)):
            if g.node_data == 
    



g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('H')

g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('B', 'H')
g.add_edge('C', 'E')
g.add_edge('C', 'D')
g.add_edge('E', 'F')
g.add_edge('E', 'G')
g.add_edge('E', 'H')

g.display()

dfs(g.graph)
print(g.node_data)