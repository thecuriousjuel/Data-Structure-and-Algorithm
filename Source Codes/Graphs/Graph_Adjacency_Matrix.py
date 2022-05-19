class Graph:
    def __init__(self):
        self.graph = []
        self.node_data = {}
        self.size = 0


    def add_node(self, node):
        if node in self.node_data:
            print('Node is present!')
            return

        self.node_data[node] = False

        for i in self.graph:
            i.append(0)

        temp = []

        for i in self.node_data:
            temp.append(0)

        self.graph.append(temp)


    def delete_node(self, node):
        node_index = list(self.node_data).index(node)
        self.graph.pop(node_index)
        
        for i in self.graph:
            i.pop(node_index)
        
        self.node_data.pop(node)


    def add_edge(self, v1, v2):
        v1_index = list(self.node_data).index(v1)
        v2_index = list(self.node_data).index(v2)

        if self.graph[v1_index][v2_index] != 0:
            print(f'Already connected! {v1} -- {v2}')
            return

        self.graph[v1_index][v2_index] = 1
        self.graph[v2_index][v1_index] = 1
        print(f'Edge added! {v1} -- {v2}')


    def delete_edge(self, v1, v2):
        v1_index = list(self.node_data).index(v1)
        v2_index = list(self.node_data).index(v2)

        if self.graph[v1_index][v2_index] == 0:
            print(f'No Edge present! {v1} -- {v2}')
            return 

        self.graph[v1_index][v2_index] = 0
        self.graph[v2_index][v1_index] = 0

        print(f'Edge removed! {v1} -- {v2}')


    def search(self, node):
        if node in self.node_data:
            print(f'{node} -- Node is present!')
            return

        print(f'{node} -- Node is not present!')


    def display(self):
        # print(self.graph)
        print('-' * 100)
        print('\t', end='')
        for i in self.node_data:
            print(i, end = '\t')
        print()
        
        for i in range(len(self.graph)):
            print(list(self.node_data)[i], end='\t')
            for j in range(len(self.graph[i])):
                print(self.graph[i][j], end = '\t')
            print()
        print('-' * 100)

if __name__ == '__main__':
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

    g.add_edge('A', 'B')
    # g.display()

    g.add_edge('A', 'B')
    # g.display()

    g.add_edge('C', 'B')
    # g.display()

    node = 'D'
    print(f'Adding node {node}')
    g.add_node(node)
    # g.display()

    g.add_edge('D', 'C')
    # g.display()

    g.add_edge('D', 'C')
    # g.display()

    # g.delete_edge('A', 'B')
    # g.display()

    g.delete_node('C')
    g.display()

    g.search('C')
