# -*- coding: utf-8 -*-
import sys

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
        return str(self.id) + ' connected to: ' + str([x for x in self.connectedTo])

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
               self.vertices[f].addNeighbor(t, weight)
            else: 
               return None
        else:
            return None
    def getVertices(self):
        return self.vertices.keys()
    def __iter__(self):
        return iter(self.vertices.values())
    
def getLeastValuedEdge(explored, g: Graph, v: Vertex):
    if v is None:
        return None
    
    vertexConnections = [x for x in v.getConnections()]
    shortestV = None
    shortestVWeight = None

    for op in vertexConnections:
        if (shortestV == None or v.connectedTo[op] < shortestVWeight) and op not in explored:
            shortestV = g.getVertex(op)
            shortestVWeight = v.connectedTo[op]
            
    if shortestV is not None:
        return shortestV, shortestVWeight
    else:
        return None

def djikstra (g: Graph, start: str, end: str):
    dist = dict()
    prev = dict()
    for v in g.getVertices():
        dist[v] = sys.maxsize
        prev[v] = None
    
    dist[start] = 0
    visited = [start]
    
    vertex = g.getVertex(start)
    shortest = getLeastValuedEdge(visited, g, vertex)    

    if shortest is None:
        return None
    
    v = shortest[0]
    dist[v.id] = shortest[1]
    visited.append(v.id)
    prev[v.id] = start
   
    while not visited.__contains__(end):
        vertexConnections = [x for x in v.getConnections()]

        for w in vertexConnections:
            if dist[v.id] + v.connectedTo[w] < dist[w]:
                dist[w] = dist[v.id] + v.connectedTo[w]
                prev[w] = v.id

        shortest = getLeastValuedEdge(visited, g, v)
        
        if shortest is not None:
            v = shortest[0]
            visited.append(v.id)
        else:
            returningV = v

            while shortest is None or (returningV and returningV.id == start):
                returningV = g.getVertex(prev[returningV.id])

                shortest = getLeastValuedEdge(visited, g, returningV)
                if shortest is not None:
                    v = shortest[0]
                    visited.append(v.id)

    route = {
        "path": [],
        "cost": dist[end]
    }

    at = end
    while at != start:
        route["path"].append({
            "from": prev[at],
            "to": at,
            "cost": g.getVertex(prev[at]).connectedTo[at]
        })
        at = prev[at]

    route["path"] = list(reversed(route["path"]))

    return route

def main():
    # fin = open("entrada_lista_locais.txt", "r")
    # fout = open("viagens.txt", "w")

    fin = sys.stdin
    fout = sys.stdout

    caseNum = fin.readline()
    if caseNum and int(caseNum):
        for _ in range(int(caseNum)):
            g = Graph()
            cities = fin.readline().strip().split()
            fout.write(f"Origem:{cities[0]} Destino:{cities[1]}\n")

            conections = fin.readline()
            if conections and int(conections):
                for _ in range(int(conections)):
                    connection = fin.readline().strip().split()
                    if not connection:
                        break
                    if connection[0] not in g:
                        g.addVertex(connection[0], connection[0])
                    if connection[1] not in g:
                        g.addVertex(connection[1], connection[1])
                    g.addEdge(connection[0], connection[1], float(connection[2]))

                vertexOrigin = g.getVertex(cities[0])
                if vertexOrigin:
                    edges = [x for x in vertexOrigin.getConnections()]
                    if len(edges) > 0:
                        res = djikstra(g, cities[0], cities[1])

                        if res:
                            for i in res["path"]:
                                fout.write(f"{i['from']} {i['to']} {i['cost']}\n")
                            fout.write(f"Tempo total: {res["cost"]} horas.\n")
                        else:
                            fout.write("Não há rota possível.\n")
                    else:
                        fout.write("Não há rota possível.\n")
                fout.write("\n")

    fin.close()
    fout.close()

main()