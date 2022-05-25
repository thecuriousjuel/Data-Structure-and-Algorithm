class Graph:
    def __init__(self, no_of_vertex):
        self.size = 0
        self.node_list = []
        self.graph_data = [[0 for i in range(no_of_vertex)] for j in range(no_of_vertex)]
        self.visited = [False] * no_of_vertex
        self.queue = []
        

    def add_node(self, vertex):
        self.node_list.append(vertex)


    def insert_data(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = 1


    def top_sort(self, start):
        start_index = self.node_list.index(start)

        if self.visited[start_index] == True:
            return

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] == 1 and self.visited[i] == False:
                self.top_sort(self.node_list[i])
                

        self.visited[start_index] = True
        self.queue.append(self.node_list[start_index])


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




no_of_vextex = 13
g = Graph(no_of_vextex)

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

g.insert_data('A', 'D')
g.insert_data('B', 'D')
g.insert_data('C', 'A')
g.insert_data('C', 'B')
g.insert_data('D', 'H')
g.insert_data('D', 'G')
g.insert_data('E', 'A')
g.insert_data('E', 'F')
g.insert_data('E', 'D')
g.insert_data('F', 'K')
g.insert_data('F', 'J')
g.insert_data('G', 'I')
g.insert_data('H', 'J')
g.insert_data('H', 'I')
g.insert_data('I', 'L')
g.insert_data('J', 'M')
g.insert_data('J', 'L')
g.insert_data('K', 'J')

g.display()

for i in range(no_of_vextex):
    g.top_sort(g.node_list[i])
print(g.queue[::-1])


# --------------------------------------------------------------------------------------------

# no_of_vextex = 8
# g = Graph(no_of_vextex)

# g.add_node('0')
# g.add_node('1')
# g.add_node('2')
# g.add_node('3')
# g.add_node('4')
# g.add_node('5')
# g.add_node('6')
# g.add_node('7')

# g.insert_data('1', '0')
# g.insert_data('2', '1')
# g.insert_data('3', '1')
# g.insert_data('5', '2')
# g.insert_data('5', '4')
# g.insert_data('6', '4')
# g.insert_data('6', '3')
# g.insert_data('7', '5')
# g.insert_data('7', '6')

# g.display()

# for i in range(no_of_vextex):
#     g.top_sort(g.node_list[i])
# print(g.queue[::-1])


# --------------------------------------------------------------------------------------------

# no_of_vextex = 6
# g = Graph(no_of_vextex)

# g.add_node(1)
# g.add_node(2)
# g.add_node(3)
# g.add_node(4)
# g.add_node(5)
# g.add_node(6)

# g.insert_data(1,2)
# g.insert_data(2,3)
# g.insert_data(2,4)
# g.insert_data(2,5)
# g.insert_data(4,5)
# g.insert_data(5,6)


# g.display()

# for i in range(no_of_vextex):
#     g.top_sort(g.node_list[i])
# print(g.queue[::-1])

# --------------------------------------------------------------------------------------------

# no_of_vextex = 8
# g = Graph(no_of_vextex)

# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')
# g.add_node('G')
# g.add_node('H')

# g.insert_data('A', 'B')
# g.insert_data('B', 'C')
# g.insert_data('B', 'H')
# g.insert_data('C', 'E')
# g.insert_data('E', 'D')
# g.insert_data('E', 'F')
# g.insert_data('E', 'G')
# g.insert_data('E', 'H')
# g.insert_data('H', 'D')

# g.display()

# for i in range(no_of_vextex):
#     if g.visited[i] == False:
#         g.top_sort(g.node_list[i])
#         g.queue.append(g.node_list[i])

# print(g.queue[::-1])

