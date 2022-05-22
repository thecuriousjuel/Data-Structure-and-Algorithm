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

#   node_list = [A B C D E F]

#   self.graph = [[0 0 0 0 0 1],
#                 [1 1 0 0 1 0]]

#   visted = []

#   cost = []


    def dijkstras(self, start = 0):
        cost = [float('inf')] * len(self.node_list)
        cost[start] = 0
        visited = []

        min_weight = min(cost)

        while len(visited) < len(self.node_list):

            index_with_min_weight = cost.index(min_weight)

            for i in range(len(self.graph[index_with_min_weight])):
                if self.graph[index_with_min_weight][i] != 0:
                    cost[i] = min(cost[index_with_min_weight] + self.graph[index_with_min_weight][i], cost[i])

            visited.append(self.node_list[index_with_min_weight])

            min_weight = float('inf')    
            for i in range(len(cost)):
                if self.node_list[i] in visited:
                    continue
                else:
                    if cost[i] < min_weight:
                        min_weight = cost[i]

        print(f'Starting point -> {self.node_list[start]}')
        print('Shortest Distance')
        print(end='\t')
        for i in self.node_list:
            print(i, end= '\t')
        print()
        
        print(self.node_list[start], end='\t')
        for i in cost:
            print(i, end= '\t')
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


# Undirected example

# g = Graph()
# g.add_node('0')
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_node('4')
# g.add_node('5')
# g.add_node('6')
# g.add_node('7')
# g.add_node('8')

# g.add_edge('0', '1', 4)
# g.add_edge('0', '7', 8)
# g.add_edge('1', '0', 4)
# g.add_edge('1', '2', 8)
# g.add_edge('1', '7', 11)
# g.add_edge('2', '1', 8)
# g.add_edge('2', '3', 7)
# g.add_edge('2', '5', 4)
# g.add_edge('2', '8', 2)
# g.add_edge('3', '2', 7)
# g.add_edge('3', '4', 9)
# g.add_edge('3', '5', 14)
# g.add_edge('4', '3', 9)
# g.add_edge('4', '5', 10)
# g.add_edge('5', '2', 4)
# g.add_edge('5', '3', 14)
# g.add_edge('5', '4', 10)
# g.add_edge('6', '5', 2)
# g.add_edge('6', '8', 6)
# g.add_edge('6', '7', 1)
# g.add_edge('7', '0', 8)
# g.add_edge('7', '1', 11)
# g.add_edge('7', '8', 7)
# g.add_edge('7', '6', 1)
# g.add_edge('8', '2', 2)
# g.add_edge('8', '6', 6)
# g.add_edge('8', '7', 7)

# g.display()

# g.dijkstras()


# --------------------------------------------------------

# g = Graph()
# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')

# g.add_edge('A', 'B', 50)
# g.add_edge('A', 'C', 45)
# g.add_edge('A', 'D', 10)
# g.add_edge('B', 'C', 10)
# g.add_edge('B', 'D', 15)
# g.add_edge('C', 'E', 30)
# g.add_edge('D', 'A', 10)
# g.add_edge('D', 'E', 15)
# g.add_edge('E', 'B', 20)
# g.add_edge('E', 'C', 35)
# g.add_edge('F', 'E', 3)

# g.display()

# g.dijkstras(start = 1)

# --------------------------------------------------------

# g = Graph()
# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')

# g.add_edge('A', 'B', 2)
# g.add_edge('A', 'C', 4)
# g.add_edge('B', 'C', 1)
# g.add_edge('B', 'D', 7)
# g.add_edge('C', 'E', 3)
# g.add_edge('D', 'F', 1)
# g.add_edge('E', 'D', 2)
# g.add_edge('E', 'F', 5)

# g.display()

# g.dijkstras()

# --------------------------------------------------------
g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')

g.add_edge('A', 'B', 3)
# g.add_edge('A', 'C', 8)
g.add_edge('A', 'D', 5)
g.add_edge('C', 'B', -10)
g.add_edge('D', 'C', 2)

g.display()

g.dijkstras(start=0)
# --------------------------------------------------------
