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
        if ngb in self.connectedTo:
            return self.connectedTo[ngb]
        else:
            return None

    def __str__(self):
        return f'{self.id} connected to: {list(self.connectedTo.keys())}'

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
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def addEdge(self, f, t, weight=0):
        if f not in self.vertices:
            self.addVertex(f, f)
        if t not in self.vertices:
            self.addVertex(t, t)
        self.vertices[f].addNeighbor(t, weight)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
    
def getLeastValuedEdge(explored, g: Graph, v: Vertex):
    if v is None:
        return None
    
    vertexConnections = [x for x in v.getConnections()]
    shortestV = None
    shortestVWeight = float('inf')

    for op in vertexConnections:
        if op not in explored and (shortestV is None or v.connectedTo[op] < shortestVWeight):
            shortestV = g.getVertex(op)
            shortestVWeight = v.connectedTo[op]
            
    if shortestV is not None:
        return shortestV, shortestVWeight
    else:
        return None

def djikstra(g: Graph, start: str, end: str):
    if start not in g.vertices or end not in g.vertices:
        return None

    dist = {v: sys.maxsize for v in g.getVertices()}
    prev = {v: None for v in g.getVertices()}
    
    dist[start] = 0
    visited = set()
    unvisited = set(g.getVertices())
    
    while unvisited:
        current = min(unvisited, key=lambda vertex: dist[vertex])
        if dist[current] == sys.maxsize:
            break
        
        unvisited.remove(current)
        visited.add(current)
        
        for neighbor in g.getVertex(current).getConnections():
            if neighbor in visited:
                continue
            new_dist = dist[current] + g.getVertex(current).getWeight(neighbor)
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = current
        
        if current == end:
            break

    if dist[end] == sys.maxsize:
        return None

    route = {
        "path": [],
        "cost": dist[end]
    }

    at = end
    while at is not None:
        if prev[at] is not None:
            route["path"].append({
                "from": prev[at],
                "to": at,
                "cost": g.getVertex(prev[at]).getWeight(at)
            })
        at = prev[at]

    route["path"] = list(reversed(route["path"]))

    return route

def main():
    # fin = open("entrada_lista_locais.txt", "r", encoding="utf-8")
    # fout = open("viagens.txt", "w", encoding="utf-8")

    fin = sys.stdin
    fout = sys.stdout

    caseNum = fin.readline().strip()
    if caseNum.isdigit() and int(caseNum) > 0:
        for k in range(int(caseNum)):
            g = Graph()
            cities = fin.readline().strip().split()

            if len(cities) >= 2:
                headingStr = f"Origem:{cities[0]} Destino:{cities[1]}\n"
                if k > 0:
                    headingStr = f"\n\n{headingStr}"

                fout.write(headingStr)
                conections = fin.readline()
                if conections and int(conections):
                    for _ in range(int(conections)):
                        connection = fin.readline().strip().split()
                        if len(connection) < 3:
                            fout.write("Erro: Conexão inválida")
                            continue
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
                                    fout.write(f"{i['from']} {i['to']} {round(i['cost'], 1)}\n")
                                fout.write(f"Tempo total: {round(res['cost'], 1)} horas.")
                            else:
                                fout.write("Não há rota possível.")
                        else:
                            fout.write("Não há rota possível.")
            else:
                fout.write("Erro: Entrada inválida")

    fin.close()
    fout.close()

main()