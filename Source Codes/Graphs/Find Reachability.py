class Graph:
    def __init__(self, N) -> None:
        self.graph_data = [[0 for _ in range(N)] for _ in range(N)]
        self.node_list = []
        self.removed_vertex = []
        self.visited = []


    def add_node(self, v):
        self.node_list.append(v)


    def add_edge(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = 1


    def reach(self, A, B):
        if A in self.visited:
            return 0
        self.visited.append(A)

        A_index = self.node_list.index(A)
        B_index = self.node_list.index(B)

        if self.graph_data[A_index][B_index] == 1:
            return 1

        for i in range(len(self.graph_data[A_index])):
            if self.graph_data[A_index][i] == 1:
                out = self.reach(self.node_list[i], B)
                if out == 1:
                    return out

        return 0

    
    
    def display(self):
        print('\t', end='')
        print(self.node_list)
        for i in range(len(self.graph_data)):
            print(self.node_list[i], end = '\t')
            print(self.graph_data[i])

N = 5

g = Graph(N)


g.add_node(4)
g.add_node(2)
g.add_node(5)
g.add_node(7)
g.add_node(9)

g.add_edge(2, 9)
g.add_edge(7, 2)
g.add_edge(7, 5)
g.add_edge(9, 5)


g.display()

A = 7
B = 9
out = g.reach(A, B)

print(out)