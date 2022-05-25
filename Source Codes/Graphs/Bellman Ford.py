class Graph:
    def __init__(self, no_of_vertex):
        self.size = 0
        self.node_list = []
        self.graph_data = [[0 for i in range(no_of_vertex)] for j in range(no_of_vertex)]
        self.weight = [float('inf') for i in range(no_of_vertex)]
        

    def add_node(self, vertex):
        self.node_list.append(vertex)


    def insert_data(self, v1, v2, w):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = w


    def bellman_ford(self):
        self.weight[0] = 0
        for i in range(len(self.node_list) - 1):
            for row in range(len(self.graph_data)):
                for col in range(len(self.graph_data[row])):
                    if self.graph_data[row][col] != 0:
                        if self.weight[row] + self.graph_data[row][col] < self.weight[col]:
                            self.weight[col] = self.weight[row] + self.graph_data[row][col]



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


# no_of_vextex = 4
# g = Graph(no_of_vextex)

# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)

# g.insert_data(1, 2, 4)
# g.insert_data(1, 4, 5)
# g.insert_data(2, 4, 5)
# g.insert_data(3, 2, -10)
# g.insert_data(4, 3, 3)

# g.display()
# g.bellman_ford()

# print('Starting node : ', g.node_list[0])
# for i in range(len(g.node_list)):
#     print(f'{g.node_list[i]} ------>  {g.weight[i]}')

#--------------------------------------------------------------------


no_of_vextex = 7
g = Graph(no_of_vextex)

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)

g.insert_data(1, 2, 6)
g.insert_data(1, 3, 5)
g.insert_data(1, 4, 5)
g.insert_data(2, 5, -1)
g.insert_data(3, 2, -2)
g.insert_data(3, 5, 1)
g.insert_data(4, 3, -2)
g.insert_data(4, 6, -1)
g.insert_data(5, 7, 3)
g.insert_data(6, 7, 3)

g.display()
g.bellman_ford()

print('Starting node : ', g.node_list[0])
for i in range(len(g.node_list)):
    print(f'{g.node_list[i]} ------>  {g.weight[i]}')


