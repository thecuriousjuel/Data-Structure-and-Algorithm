class Graph:
    def __init__(self):
        self.graph = []
        self.node_list = []
        self.size = 0


    def add_node(self, node):
        if node in self.node_list:
            print('Node is present!')
            return

        self.node_list.append(node)

        for i in self.graph:
            i.append(0)

        temp = []

        for i in self.node_list:
            temp.append(0)

        self.graph.append(temp)


    def delete_node(self, node):
        node_index = self.node_list.index(node)
        self.graph.pop(node_index)
        
        for i in self.graph:
            i.pop(node_index)
        
        self.node_list.pop(node_index)


    def add_edges(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        if self.graph[v1_index][v2_index] != 0:
            print('Already connected! {v1} -- {v2}')
            return

        self.graph[v1_index][v2_index] = 1
        self.graph[v2_index][v1_index] = 1
        print(f'Edge added! {v1} -- {v2}')


    def delete_edges(self, v1, v2):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        if self.graph[v1_index][v2_index] == 0:
            print(f'No Edge present! {v1} -- {v2}')
            return 

        self.graph[v1_index][v2_index] = 0
        self.graph[v2_index][v1_index] = 0

        print(f'Edge removed! {v1} -- {v2}')
        

    def display(self):
        # print(self.graph)
        print('-' * 20)
        print('\t', end='')
        for i in self.node_list:
            print(i, end = '\t')
        print()
        
        for i in range(len(self.graph)):
            print(self.node_list[i], end='\t')
            for j in range(len(self.graph[i])):
                print(self.graph[i][j], end = '\t')
            print()
        print('-' * 20)


g = Graph()

node = 'A'
print(f'Adding node {node}')
g.add_node(node)
# g.display()

node = 'B'
print(f'Adding node {node}')
g.add_node(node)
# g.display()

node = 'C'
print(f'Adding node {node}')
g.add_node(node)
# g.display()

g.add_edges('A', 'B')
# g.display()

g.add_edges('A', 'B')
# g.display()

g.add_edges('C', 'B')
# g.display()

node = 'D'
print(f'Adding node {node}')
g.add_node(node)
# g.display()

g.add_edges('D', 'C')
# g.display()

g.add_edges('D', 'C')
g.display()

g.delete_node('C')
g.display()