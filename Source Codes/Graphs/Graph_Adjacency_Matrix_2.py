class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False


    def add_neighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)

    def getConenctions(self, G):
        return G.adjMatrix[self.id]

    def getVertex_ID(self):
        return self.id

    def setVertex_ID(self, id):
        self.id = id

    def setVisited(self):
        self.visited = True

    def __str__(self) -> str:
        return str(self.id)


class Graph:
    def __init__(self, numVertices, cost = 0):
        self.adjMatrix = [[-1] * numVertices for _ in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []

        for i in range(numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)

        
    def setVertex(self, vtx, id):
        if 0 <= vtx < self.numVertices:
            self.vertices[vtx].setVertex_ID(id)


    def getVertex(self, n):
        for vertex in range(self.numVertices):
            if n == self.vertices[vertex].getVertex_ID():
                return vertex

        else:
            return -1

    
    def addEdge(self, frm, to, cost=0):
        if self.getVertex(frm)!= -1 and self.getVertex(to) != -1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost


    def getEdges(self):
        edges = []
        for v in range(self.numVertices):
            for u in range(self.numVertices):
                if self.adjMatrix[u][v] != 1:
                    vid = self.vertices[v].getVertex_ID()
                    wid = self.vertices[u].getVertex_ID()
                    edges.append((vid, wid, self.adjMatrix[u][v]))
        return edges 

    
    def getVertices(self):
        vertices = []

        for vertex in range(self.numVertices):
            vertices.append(self.vertices[vertex].getVertex_ID())

        return vertices


    def printMatrix(self):
        for u in range(self.numVertices):
            row = []
            for v in range(self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)


if __name__ == '__main__':
    G = Graph(5)

    G.setVertex(0, 'a')
    G.setVertex(1, 'b')
    G.setVertex(2, 'c')
    G.setVertex(3, 'd')
    G.setVertex(4, 'e')

    print('Graph Data')

    G.addEdge('a', 'e', 10)
    G.addEdge('a', 'c', 20)
    G.addEdge('c', 'b', 30)
    G.addEdge('b', 'e', 40)
    G.addEdge('e', 'd', 50)
    G.addEdge('f', 'e', 60)
    G.printMatrix()
    print(G.getEdges())