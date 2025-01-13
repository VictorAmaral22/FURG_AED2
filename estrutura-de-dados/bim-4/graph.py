class Vertex:
    def __init__(self, key, value):
        self.id = key
        self.value = value
        self.connectedTo = {}

    def addNeighbor(self, ngb, weight=0):
        self.connectedTo[ngb] = weight
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getValue(self):
        return self.value
    def getWeight(self, ngb):
        return self.connectedTo[ngb]
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key, value):
        self.numVertices += 1
        newVertex = Vertex(key, value)
        self.vertices[key] = newVertex
        return newVertex
    def getVertex(self, key):
        if self.vertices[key]:
            return self.vertices[key]
        else:
            return None
    def __contains__(self, key):
        return key in self.vertices
    def addEdge(self, f, t, weight=0):
        if f in self.vertices and t in self.vertices:
            fromVertex = self.vertices[f]
            if t not in fromVertex.connectedTo:
               self.vertices[f].addNeighbor(self.vertices[t], weight)
            else: 
               return None
        else:
            return None
    def getVertices(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())

g = Graph()
for i in range(6):
    g.addVertex(i, "V"+str(i))
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print("(%s, %s, %s)" % (v.getId(), w.getId(), v.getWeight(w)))