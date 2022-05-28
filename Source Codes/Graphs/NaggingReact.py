class Graph:
    def __init__(self, N) -> None:
        self.graph_data = [[0 for _ in range(N)] for _ in range(N)]
        self.node_list = []
        self.removed_vertex = []


    def add_node(self, v):
        self.node_list.append(v)


    def add_edge(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = 1


    def remove_connected(self, A, B):
        A_index = self.node_list.index(A)
        B_index = self.node_list.index(B)

        for i in range(len(self.graph_data[A_index])):
            if self.graph_data[A_index][i] == 1:

                if self.node_list[i] == B:
                    self.removed_vertex.append(self.node_list[A_index])
                    self.graph_data[A_index][i] = 0

                self.remove_connected(self.node_list[i], B)

    
    def display(self):
        print('\t', end='')
        print(self.node_list)
        for i in range(len(self.graph_data)):
            print(self.node_list[i], end = '\t')
            print(self.graph_data[i])

N = 5

g = Graph(N)


g.add_node(2)
g.add_node(5)
g.add_node(6)
g.add_node(7)
g.add_node(9)

g.add_edge(2, 5)
g.add_edge(5, 9)
g.add_edge(6, 5)
g.add_edge(6, 7)
g.add_edge(6, 9)
g.add_edge(9, 7)

g.display()

A = 2
B = 7
g.remove_connected(A, B)

print(g.removed_vertex)