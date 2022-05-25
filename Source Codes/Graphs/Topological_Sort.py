class Graph:
    # Directed Graph
    
    
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
        print(f'Edge added! {v1} -- {v2}')


    # def dfs(self, root):
    #     node_index = self.node_list.index(root)
    #     print(root, end= ' ')
    #     self.visited[node_index] = True

    #     for i in range(len(self.graph[node_index])):
    #         if self.graph[node_index][i] == 1 and self.visited[i] == False:
    #             self.dfs(self.node_list[i])


    def dfs(self, root):
        
        node_index = self.node_list.index(root)
        if self.visited[node_index] == True:
            return

        for i in range(len(self.graph[node_index])):
            if self.graph[node_index][i] == 1 and self.visited[i] == False:
                self.dfs(self.node_list[i])

        self.visited[node_index] = True
        self.stack.insert(0, root)


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

# ----------------------------------------------------------------------------

# g = Graph()
# g.add_node('0')
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_node('4')
# g.add_node('5')
# g.add_node('6')
# g.add_node('7')

# g.add_edge('1', '0')
# g.add_edge('2', '1')
# g.add_edge('3', '1')
# g.add_edge('5', '2')
# g.add_edge('5', '4')
# g.add_edge('6', '4')
# g.add_edge('6', '3')
# g.add_edge('7', '5')
# g.add_edge('7', '6')

# print('Topological Sorting -> ', end = ' ')

# # setting the starting node
# g.stack = []
# for i in range(len(g.node_list)):
#     g.dfs(g.node_list[i])
# print(g.stack)

# ----------------------------------------------------------------------------

# g = Graph()
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_node('4')
# g.add_node('5')

# g.add_edge('1', '2')
# g.add_edge('1', '4')
# g.add_edge('2', '3')
# g.add_edge('2', '4')
# g.add_edge('3', '5')
# g.add_edge('4', '3')

# print('Topological Sorting -> ', end = ' ')

# # setting the starting node
# g.stack = []
# for i in range(len(g.node_list)):
#     g.dfs(g.node_list[i])
# print(g.stack)

# ----------------------------------------------------------------------------
# g = Graph()
# g.add_node('0')
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_node('4')
# g.add_node('5')

# g.add_edge('2', '3')
# g.add_edge('3', '1')
# g.add_edge('4', '0')
# g.add_edge('4', '1')
# g.add_edge('5', '0')
# g.add_edge('5', '2')

# print('Topological Sorting -> ', end = ' ')

# # setting the starting node
# g.stack = []
# for i in range(len(g.node_list)):
#     g.dfs(g.node_list[i])
# print(g.stack)

# ----------------------------------------------------------------------------

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')
g.add_node('G')
g.add_node('H')
g.add_node('I')
g.add_node('J')
g.add_node('K')
g.add_node('L')
g.add_node('M')

g.add_edge('A', 'D')
g.add_edge('B', 'D')
g.add_edge('C', 'A')
g.add_edge('C', 'B')
g.add_edge('D', 'H')
g.add_edge('D', 'G')
g.add_edge('E', 'A')
g.add_edge('E', 'F')
g.add_edge('E', 'D')
g.add_edge('F', 'K')
g.add_edge('F', 'J')
g.add_edge('G', 'I')
g.add_edge('H', 'J')
g.add_edge('H', 'I')
g.add_edge('I', 'L')
g.add_edge('J', 'M')
g.add_edge('J', 'L')
g.add_edge('K', 'J')

print('Topological Sorting -> ', end = ' ')

# setting the starting node
g.stack = []
for i in range(len(g.node_list)):
    g.dfs(g.node_list[i])
print(g.stack)


# ----------------------------------------------------------------------------


# g = Graph()
# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')
# g.add_node('G')
# g.add_node('H')

# g.add_edge('A', 'B')
# g.add_edge('B', 'C')
# g.add_edge('B', 'H')
# g.add_edge('C', 'E')
# g.add_edge('C', 'D')
# g.add_edge('E', 'F')
# g.add_edge('E', 'G')
# g.add_edge('E', 'H')
# g.add_edge('H', 'D')

# print('Topological Sorting -> ', end = ' ')

# # setting the starting node
# g.stack = []
# for i in range(len(g.node_list)):
#     g.dfs(g.node_list[i])
# print(g.stack)

# g.visited = [False for i in range(len(g.visited))]



