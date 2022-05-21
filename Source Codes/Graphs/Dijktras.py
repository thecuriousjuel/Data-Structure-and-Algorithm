class Graph:
    # Directed and weighted Graph
    
    
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


    def add_edge(self, v1, v2, w):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        if self.graph[v1_index][v2_index] != 0:
            print(f'Already connected! {v1} -- {v2}')
            return

        self.graph[v1_index][v2_index] = w
        print(f'Edge added! {v1} -- {v2}')


    def dijkstras(self):
        queue = [self.node_list[0]]
        
        cost = [float('inf')] * len(self.node_list)

        current = queue[0]
        node_index = self.node_list.index(current)
        cost[node_index] = 0
        self.visited[node_index] = True

        print([i for i in self.node_list])

        while len(queue) > 0:
            print(cost)
            
            current = queue[0]
            node_index = self.node_list.index(current)

            for i in range(len(self.graph[node_index])):
                if self.graph[node_index][i] > 0 and self.visited[i] == False:
                    cost[i] = min(self.graph[node_index][i] + cost[node_index], cost[i])
                    queue.append(self.node_list[i])

                    self.visited[i] = True

            queue = queue[1:]
            
        print()



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




# g = Graph()
# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')

# g.add_edge('A', 'B', 50)
# g.add_edge('A', 'C', 45)
# g.add_edge('A', 'D', 40)
# g.add_edge('B', 'C', 10)
# g.add_edge('B', 'D', 15)
# g.add_edge('C', 'E', 30)
# g.add_edge('D', 'A', 10)
# g.add_edge('D', 'E', 15)
# g.add_edge('E', 'B', 20)
# g.add_edge('E', 'C', 35)
# g.add_edge('F', 'E', 3)

# g.display()

# g.dijkstras()

# --------------------------------------------------------
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')

g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 7)
g.add_edge('C', 'E', 3)
g.add_edge('D', 'F', 1)
g.add_edge('E', 'D', 2)
g.add_edge('E', 'F', 5)

g.display()

g.dijkstras()

# --------------------------------------------------------
# g = Graph()
# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')

# g.add_edge('A', 'B', 3)
# # g.add_edge('A', 'C', 8)
# g.add_edge('A', 'D', 5)
# g.add_edge('C', 'B', 3)
# g.add_edge('D', 'C', 2)

# g.display()

# g.dijkstras()
# --------------------------------------------------------
