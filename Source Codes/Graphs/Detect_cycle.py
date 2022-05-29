class Solution:
    
    #Function to detect cycle in a directed graph.
    def __init__(self):
        self.node_list = []
        self.graph_data = {}
    
    
    def add_node(self, V):
        for i in range(V):
            self.node_list.append(i)
            
            
    def is_cyclic_helper(self, start, path = []):
        print(start, path)
        start_index = start
        
        if start in path:
            return 1
            
        path.append(start)
        
        for i in self.graph_data[start_index]:
            l = self.is_cyclic_helper(i, path[:])
            if l == 1:
                return 1
        
        
    def isCyclic(self, V, adj):
        self.add_node(V)
        
        for i in range(len(adj)):
            self.graph_data[i] = adj[i]
            
        # print(adj)
        print(self.graph_data)
        
        if len(self.node_list) == 0:
            return 0
            
            
        for i in self.node_list:
            l = self.is_cyclic_helper(i, []) 
            print(l)
            print('-' * 10)
            if l == 1:
                return 1



adj = [[], [2], [4], [1], [0], [3]]

print(adj)

ob = Solution()
out = ob.isCyclic(V=6, adj=adj)

print(out)
