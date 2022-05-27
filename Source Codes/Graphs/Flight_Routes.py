class Graph:
    def __init__(self, v):
        self.graph_data = [[0 for i in range(v)] for j in range(v)]
        self.node_list = []
        self.visited = [False] * v
        self.connected = False
        self.all_paths = []
        self.min_path_distance = float('inf')
        self.min_path = []


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


    def get_all_routes(self, start, stop, path=[]):
        path.append(start)

        start_index = self.node_list.index(start)
        stop_index = self.node_list.index(stop)

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] != 0:

                if i == stop_index:
                    path.append(stop)
                    self.all_paths.append(path[:])

                else:
                    if path[-1] == stop:
                        path.pop()
                    self.get_all_routes(self.node_list[i], stop, path[:])



    def all_distances(self, start, stop, path=[], d = 0):
        path.append(start)

        # print(start, stop, d)

        start_index = self.node_list.index(start)
        stop_index = self.node_list.index(stop)

        for i in range(len(self.graph_data[start_index])):
            if self.graph_data[start_index][i] != 0:
                
                if self.node_list[i] == stop:
                    path.append(stop)
                    print(path, d+self.graph_data[start_index][i])

                    if  d+self.graph_data[start_index][i] < self.min_path_distance:
                        self.min_path_distance = d+self.graph_data[start_index][i]
                        self.min_path = path

                    if i < len(self.node_list) - 1:
                        path = path[:-1]

                self.all_distances(self.node_list[i], stop, path[:], d+self.graph_data[start_index][i])



    def display(self):
        print('\t', end='')

        for i in self.node_list:
            print(i, end='\t')
        print()

        for row in range(len(self.graph_data)):
            print(self.node_list[row], end='\t')
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


# src = 'Tor'
# dest = 'Par'
# g.get_all_routes(src, dest)
# print(f'Source : {src}. Destination {dest}.')
# for path in range(len(g.all_paths)):
#     print(f'Path {path+1} : {g.all_paths[path]}')


src = 'Mum'
dest = 'Tor'
print(f'All the Paths from {src} to {dest} with their distances.')
print('-' * 50)
g.all_distances(src, dest)
print('-' * 50)

print('Minimum Distance and the Route')
print(g.min_path_distance, g.min_path)
