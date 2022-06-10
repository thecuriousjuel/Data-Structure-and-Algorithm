class Graph:
    def __init__(self, num_of_vertex):
        self.vertex_list = []
        self.graph = [[0 for _ in range(num_of_vertex)] for _ in range(num_of_vertex)]
        self.visited = [0 for _ in range(num_of_vertex)]


    def add_vertex(self, vertex):
        self.vertex_list.append(vertex)


    def add_edge(self, v1, v2):
        v1_index = self.vertex_list.index(v1)
        v2_index = self.vertex_list.index(v2)

        self.graph[v1_index][v2_index] = 1


    def display(self):
        print('\t', end='')
        for i in self.vertex_list:
            print(i, end='\t')
        print()

        for i in range(len(self.graph)):
            print(self.vertex_list[i], end='\t')
            for j in range(len(self.graph[i])):
                print(self.graph[i][j], end='\t')
            print()


n=4
g = Graph(n)
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'A')
g.add_edge('C', 'D')
g.add_edge('D', 'A')
g.add_edge('D', 'B')

# g.add_edge('A', 'C')
# g.add_edge('B', 'A')
# g.add_edge('C', 'B')
# g.add_edge('C', 'D')


print('-----You are working on this!-----')
g.display()
