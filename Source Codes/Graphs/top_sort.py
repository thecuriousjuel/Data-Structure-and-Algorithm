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
        self.graph_data[v2_index][v1_index] = 1


    def top_sort(self, start):
        start_index = self.node_list.index(start)

        for i in range(len(self.graph_data[start_index])):
            print(self.queue, self.graph_data[start_index][i], self.visited[i])
            if self.graph_data[start_index][i] == 1 and self.visited[i] == False:
                self.visited[i] = True
                self.top_sort(self.node_list[i])

        self.queue.append(start)


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




no_of_vextex = 6
g = Graph(no_of_vextex)

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)

g.insert_data(1,2)
g.insert_data(1,3)
g.insert_data(2,4)
g.insert_data(2,5)
g.insert_data(3,5)
g.insert_data(4,5)
g.insert_data(4,6)
g.insert_data(5,6)


g.display()

for i in range(no_of_vextex):
    g.top_sort(g.node_list[i])

# print(g.queue)
