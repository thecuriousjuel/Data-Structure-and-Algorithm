class Graph:
    def __init__(self, v) -> None:
        self.graph_data = [[0 for i in range(v)] for j in range(v)]
        self.node_list = []
        self.visited = [False] * v
        self.connected = False
        self.path = []


    def add_vertex(self, v):
        self.node_list.append(v)


    def add_edges(self, v1, v2, w):
        v1_index = self.node_list.index(v1)
        v2_index = self.node_list.index(v2)

        self.graph_data[v1_index][v2_index] = w


    def is_path_present(self, start, stop):
        self.path.append(start)

        start_index = self.node_list.index(start)
        stop_index = self.node_list.index(stop)

        if self.graph_data[start_index][stop_index] != 0:
            self.connected = True
            self.path.append(stop)
            return


        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] != 0 and self.visited[i] == False:
                self.visited[start_index] = True
                return self.is_path_present(self.node_list[i], stop)


        
    def get_all_routes(self, start, stop, path = []):
        path.append(start)
        print(1, start, stop, path)

        start_index = self.node_list.index(start)
        stop_index = self.node_list.index(stop)

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] != 0 and self.visited[i] == False:
                

                if i == stop_index:
                    path.append(stop)
                    print(2, start, stop, path)
                    print('-' * 10)               
                else:
                    self.get_all_routes(self.node_list[i], stop, path)
                    self.visited[start_index] = True
                    print(3, start, stop, path)

                
            
    
    def display(self):
        print('\t', end = '')

        for i in self.node_list:
            print(i, end = '\t')
        print()

        for row in range(len(self.graph_data)):
            print(self.node_list[row], end = '\t')
            for col in range(len(self.graph_data[row])):
                print(self.graph_data[row][col], end='\t')
            print()



no_of_vertex = 7

g = Graph(no_of_vertex)

g.add_vertex('Mum')
g.add_vertex('Bos')
g.add_vertex('Har')
g.add_vertex('Par')
g.add_vertex('NY')
g.add_vertex('Dub')
g.add_vertex('Tor')

g.add_edges('Mum', 'Bos', 5000)
g.add_edges('Mum', 'Par', 4000)
g.add_edges('Mum', 'Dub', 500)
g.add_edges('Bos', 'Har', 200)
g.add_edges('Har', 'NY', 100)
g.add_edges('NY', 'Tor', 400)
g.add_edges('Par', 'Dub', 2000)
g.add_edges('Par', 'NY', 3000)
g.add_edges('Dub', 'NY', 6000)

g.display()

# src = 'Mum'
# dest = 'Tor'
# g.is_path_present(src, dest)
# if g.connected == False:
#     g.path = []
# print(f'{src} -- {dest}. Connected : {g.connected}')
# print(f'Path Taken : {g.path}')



src = 'Mum'
dest = 'NY'
g.get_all_routes(src, dest)
print(f'Path Taken : {g.path}')

