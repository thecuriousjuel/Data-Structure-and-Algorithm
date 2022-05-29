class Graph:
    def __init__(self, N) -> None:
        self.graph_data = [[0 for _ in range(N)] for _ in range(N)]
        self.node_list = []
        self.removed_vertex = []
        self.visited = []
        self.path_distances = float('inf')


    def add_node(self, v):
        self.node_list.append(v)


    def add_edge(self, v1, v2, t1):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = t1
   
    # Working for both acyclic and cyclic graphs.
    def learn_js(self, A, B, path = [], d = 0):
        A_index = self.node_list.index(A)
        B_index = self.node_list.index(B)

        if A in path:
            return

        path.append(A)

        for i in range(len(self.graph_data[A_index])):
            if self.graph_data[A_index][i] != 0:

                if self.node_list[i] == B:
                    if d + self.graph_data[A_index][i] < self.path_distances:
                        self.path_distances = d + self.graph_data[A_index][i]
                else:
                    self.learn_js(self.node_list[i], B, path[:], d + self.graph_data[A_index][i])



    def display(self):
        print('\t', end='')
        print(self.node_list)
        for i in range(len(self.graph_data)):
            print(self.node_list[i], end = '\t')
            print(self.graph_data[i])



N = 4

g = Graph(N)

g.add_node(2)
g.add_node(5)
g.add_node(7)
g.add_node(9)

g.add_edge(2, 9, 2)
g.add_edge(7, 2, 3)
g.add_edge(7, 9, 7)
g.add_edge(9, 5, 1)


g.display()

A = 7
B = 9

g.learn_js(A, B)

print(g.path_distances)

#-------------------------------------------------------------
# N = 6

# g = Graph(N)


# g.add_node(2)
# g.add_node(5)
# g.add_node(6)
# g.add_node(7)
# g.add_node(8)
# g.add_node(9)

# g.add_edge(2, 5, 5)
# g.add_edge(2, 7, 15)
# g.add_edge(5, 9, 4)
# g.add_edge(5, 6, 2)
# g.add_edge(6, 2, 3)
# g.add_edge(6, 8, 1)
# g.add_edge(8, 7, 2)
# g.add_edge(9, 8, 3)

# g.display()

# A = 2
# B = 6

# g.learn_js(A, B)

# print(g.path_distances)