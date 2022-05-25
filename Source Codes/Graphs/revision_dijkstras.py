class Graph:
    def __init__(self, no_of_vertex):
        self.size = 0
        self.node_list = []
        self.graph_data = [[0 for i in range(no_of_vertex)] for j in range(no_of_vertex)]
        self.visited = []
        self.weight = [float('inf') for i in range(no_of_vertex)]
        

    def add_node(self, vertex):
        self.node_list.append(vertex)


    def insert_data(self, v1, v2, w):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = w


    def dijkstras(self, start):
        q_index = self.node_list.index(start)
        self.weight[q_index] = 0

        while len(self.visited) < len(self.node_list):


            min_value = float('inf')
            temp_index = 0

            for i in range(len(self.node_list)):
                if self.node_list[i] in self.visited:
                    continue

                if self.weight[i] < min_value:
                    min_value = self.weight[i]
                    temp_index = i

            for i in range(len(self.graph_data[temp_index])):
                if self.graph_data[temp_index][i] > 0 and self.node_list[i] not in self.visited:
                    if self.weight[temp_index] + self.graph_data[temp_index][i] < self.weight[i]:
                        self.weight[i] = self.weight[temp_index] + self.graph_data[temp_index][i]

            self.visited.append(self.node_list[temp_index])


    def display(self):
        print('\t', end = '')
        for i in self.node_list:
            print(i, end = '\t')
        print()

        for i in range(len(self.graph_data)):
            print(self.node_list[i], end = '\t')
            for j in range(len(self.graph_data[i])):
                print(self.graph_data[i][j], end = '\t')

            print()




# no_of_vextex = 5
# g = Graph(no_of_vextex)

# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')

# g.insert_data('A', 'B', 10)
# g.insert_data('A', 'C', 3)
# g.insert_data('B', 'E', 15)
# g.insert_data('C', 'B', 4)
# g.insert_data('C', 'E', 5)
# g.insert_data('C', 'D', 6)

# g.display()
# g.dijkstras(g.node_list[0])
# print(g.weight)

# --------------------------------------------------------------------------------------------

no_of_vextex = 9
g = Graph(no_of_vextex)


g.add_node('0')
g.add_node('1')
g.add_node('2')
g.add_node('3')
g.add_node('4')
g.add_node('5')
g.add_node('6')
g.add_node('7')
g.add_node('8')

g.insert_data('0', '1', 4)
g.insert_data('0', '7', 8)
g.insert_data('1', '0', 4)
g.insert_data('1', '2', 8)
g.insert_data('1', '7', 11)
g.insert_data('2', '1', 8)
g.insert_data('2', '3', 7)
g.insert_data('2', '5', 4)
g.insert_data('2', '8', 2)
g.insert_data('3', '2', 7)
g.insert_data('3', '4', 9)
g.insert_data('3', '5', 14)
g.insert_data('4', '3', 9)
g.insert_data('4', '5', 10)
g.insert_data('5', '2', 4)
g.insert_data('5', '3', 14)
g.insert_data('5', '4', 10)
g.insert_data('6', '5', 2)
g.insert_data('6', '8', 6)
g.insert_data('6', '7', 1)
g.insert_data('7', '0', 8)
g.insert_data('7', '1', 11)
g.insert_data('7', '8', 7)
g.insert_data('7', '6', 1)
g.insert_data('8', '2', 2)
g.insert_data('8', '6', 6)
g.insert_data('8', '7', 7)


g.display()
g.dijkstras(g.node_list[0])
print(g.weight)