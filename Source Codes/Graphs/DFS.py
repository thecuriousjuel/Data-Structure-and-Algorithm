class Graph:
    def __init__(self):
        self.graph = []
        self.node_list = []
        self.visited = []
        self.size = 0


    def add_node(self, node):
        if node in self.node_list:
            print('Node is present!')
            return

        self.node_list.append(node)
        self.visited.append(False)

        for i in self.graph:
            i.append(0)

        temp = []

        for i in self.node_list:
            temp.append(0)

        self.graph.append(temp)


    def add_edge(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        if self.graph[v1_index][v2_index] != 0:
            print(f'Already connected! {v1} -- {v2}')
            return

        self.graph[v1_index][v2_index] = 1
        self.graph[v2_index][v1_index] = 1
        print(f'Edge added! {v1} -- {v2}')


    def dfs(self, root):
        # case 1: If there is a dead end
        # case 2: If the node is already visited
        # case 3: If there are many unvisited nodes
        # case 4: If there are many visited nodes

        node_index = self.node_list.index(root)
        print(root, end = ' ')
        self.visited[node_index] = True

        
        for index in range(len(self.graph[node_index])):
            if self.graph[node_index][index] == 1 and self.visited[index] == False:
                self.dfs(self.node_list[index])


    def display(self):
        # print(self.graph)
        print('-' * 100)
        print('\t', end='')
        for i in self.node_list:
            print(i, end = '\t')
        print()
        
        for i in range(len(self.graph)):
            print(self.node_list[i], end='\t')
            for j in range(len(self.graph[i])):
                print(self.graph[i][j], end = '\t')
            print()
        print('-' * 100)

   
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
# g.add_edge('B', 'C')
g.add_edge('B', 'H')
g.add_edge('C', 'E')
g.add_edge('C', 'D')
g.add_edge('E', 'F')
g.add_edge('E', 'G')
g.add_edge('E', 'H')

g.display()

# print(g.graph)

g.dfs(g.node_list[0])
# print(g.node_data)