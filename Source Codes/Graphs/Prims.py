class Graph:
    def __init__(self, N) -> None:
        self.graph_data = [[0 for _ in range(N)] for _ in range(N)]
        self.node_list = []
        self.weights = [float('inf') for _ in range(N)]
        self.visited = []
        self.mst = [[0 for _ in range(N)] for _ in range(N)]


    def add_node(self, v):
        self.node_list.append(v)


    def add_edge(self, v1, v2, t1):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = t1
        self.graph_data[v2_index][v1_index] = t1


    def prims(self):
        start_index = 0
        
        min_value = float('inf')

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] != 0 and self.visited[i] == False:
                if self.graph_data[start_index][i] < min_value:
                    min_value = self.graph_data[start_index][i]
                    start_index = i

        self.visited[start_index] = True
           

    def display(self):
        print('\t', end='')
        for i in self.node_list:
            print(i, end='\t')
        print()

        for i in range(len(self.graph_data)):
            print(self.node_list[i], end = '\t')
            for j in self.graph_data[i]:
                print(j, end='\t')
            print()


    def display_mst(self):
        print('\t', end='')
        for i in self.node_list:
            print(i, end='\t')
        print()

        for i in range(len(self.mst)):
            print(self.node_list[i], end = '\t')
            for j in self.mst[i]:
                print(j, end='\t')
            print()
            





# -------------------------------------------------------------------------------
N = 5

g = Graph(N)

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')

g.add_edge('A', 'B', 2)
g.add_edge('A', 'E', 3)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 6)
g.add_edge('B', 'E', 5)
g.add_edge('C', 'D', 7)
g.add_edge('D', 'E', 4)

g.display()

g.weights[0] = 0
g.prims()
print(g.weights)

g.display_mst()