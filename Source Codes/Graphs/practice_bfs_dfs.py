class Graph:
    def __init__(self, no_of_vertex):
        self.size = 0
        self.node_list = []
        self.graph_data = [[0 for i in range(no_of_vertex)] for j in range(no_of_vertex)]
        self.visited = [False] * no_of_vertex
        

    def add_node(self, vertex):
        self.node_list.append(vertex)


    def insert_data(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = 1
        self.graph_data[v2_index][v1_index] = 1


    def dfs(self, start):
        start_index = self.node_list.index(start)

        print(start, end= ' ')
        self.visited[start_index] = True

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] == 1 and self.visited[i] == False:
                self.dfs(self.node_list[i])

    
    def bfs(self, start):
        queue = [start]

        while len(queue) > 0:

            start_index = self.node_list.index(queue[0])
            self.visited[start_index] = True

            print(queue[0], end = ' ')

            for i in range(len(self.graph_data[start_index])):
                if self.graph_data[start_index][i] == 1 and self.visited[i] == False:
                    self.visited[i] = True
                    queue.append(self.node_list[i])

            queue = queue[1:]
                


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

g.dfs(g.node_list[0])
print()

g.visited = [False] * no_of_vextex
g.bfs(g.node_list[0])
print()


# --------------------------------------------------------
# A B C D E


# A ----- B ----- D
# |             
# |        
# C ------- E  

# no_of_vextex = 7
# g = Graph(no_of_vextex)

# g.add_node('A')
# g.add_node('B')
# g.add_node('C')
# g.add_node('D')
# g.add_node('E')
# g.add_node('F')
# g.add_node('G')

# g.insert_data('A', 'A')
# g.insert_data('A', 'D')
# g.insert_data('A', 'G')
# g.insert_data('B', 'E')
# g.insert_data('B', 'F')
# g.insert_data('C', 'D')
# g.insert_data('D', 'E')
# g.insert_data('E', 'F')
# g.insert_data('F', 'G')

# g.dfs(g.node_list[0])
# print()

# g.visited = [False] * no_of_vextex
# g.bfs(g.node_list[0])
# print()