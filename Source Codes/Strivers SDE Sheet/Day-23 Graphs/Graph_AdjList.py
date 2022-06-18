class Graph:
    def __init__(self):
        self.graph_data = {}
        self.node_list = []
        
        
    def add_vertex(self, vertex):
        self.graph_data[vertex] = []
        self.node_list.append(vertex)
        
        
    def add_edges(self, e1, e2):
        self.graph_data[e1].append(e2)
        
        
    def display(self):
        for key, value in self.graph_data.items():
            print(f'{key}-> {value}') 
    
    
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

g.add_edges('A', 'B')
g.add_edges('A', 'D')
g.add_edges('B', 'A')
g.add_edges('B', 'D')
g.add_edges('B', 'E')
g.add_edges('C', 'E')
g.add_edges('D', 'A')
g.add_edges('D', 'B')
g.add_edges('E', 'B')
g.add_edges('E', 'C')
    
g.display()
    
    
    
    
    
    
    
    
    
    
    