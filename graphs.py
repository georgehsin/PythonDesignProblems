import sys
from operator import itemgetter

class Graph:
    def __init__(self):
        self.verticies = {}
        self.verticiesCount = 0

    def addVertex(self, key):
        self.verticiesCount += 1
        newVertex = Vertex(key)
        self.verticies[key] = newVertex
        return newVertex

    def getVertex(self, key):
        if key in self.verticies:
            return self.verticies[key]
        else:
            return None

    def addEdge(self, fromEdge, toEdge, weight=0):
        if fromEdge not in self.verticies:
            self.addVertex(fromEdge)
        if toEdge not in self.verticies:
            self.addVertex(toEdge)
        self.verticies[fromEdge].addEdge(self.verticies[toEdge], weight)
        # Uncomment below when using Undirected Graphs
        # self.verticies[toEdge].addEdge(self.verticies[fromEdge], weight)

    def __iter__(self):
        return iter(self.verticies.values())

    def getVerticies(self):
        return self.verticies.keys()

    def transpose(self):
        # iterate through VERTEX for all verticies:
        #     make copy of adjacent neighbors
        #     delete current adjacent neighbors
        #     interate through each NEIGHBOR for copy of adjacent neighbors:
        #         addEdge(NEIGHBOR, VERTEX.id)

        # self.verticies = {}
        # self.verticiesCount = 0
        for vertex in self.__iter__():
            oldAdjacent = vertex.getAdjacent()
            vertex.adjacent = {}            
            for adj in oldAdjacent:
                # addEdge(adj.id, vertex.id)




class Vertex:
    def __init__(self, key):
        self.id = key
        self.adjacent = {}
        self.color = 'white'
        self.prev = None
        self.distance = sys.maxsize
        self.start = 0
        self.stop = 0

    def addEdge(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def getAdjacent(self):
        return self.adjacent.keys()

    def getWeight(self, vertex):
        return self.adjacent[vertex]

    def setColor(self, color):
        self.color = color

    def setPrev(self, vertex):
        self.prev = vertex

    def setDistance(self, distance):
        self.distance = distance

    def setStart(self, time):
        self.start = time

    def setStop(self, time):
        self.stop = time

# DEPTH FIRST SEARCH
class DFSGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.time = 0
        self.finishTimes = []

    def dfs(self):
        for v in self:
            v.setColor('white')
            v.setPrev(-1)
        for v in self:
            if v.color == 'white':
                self.dfsVisit(v)

    def dfsVisit(self, vertex):
        vertex.setColor('grey')
        self.time += 1
        vertex.setStart(self.time)
        for adjacent in vertex.getAdjacent():
            if adjacent.color == 'white':
                adjacent.setPrev(vertex)
                self.dfsVisit(adjacent)
        vertex.setColor('black')
        self.time += 1
        self.finishTimes.append((self.time, vertex))
        vertex.setStop(self.time)

    def topologicalSort(self):
        self.finishTimes.sort(key=itemgetter(0) ,reverse = True)
        return self.finishTimes




g = Graph()

g.addVertex('a')
g.addVertex('b')
g.addVertex('c')
g.addVertex('d')
g.addVertex('e')
g.addVertex('f')

g.addEdge('a', 'b', 7)  
g.addEdge('a', 'c', 9)
g.addEdge('a', 'f', 14)
g.addEdge('b', 'c', 10)
g.addEdge('b', 'd', 15)
g.addEdge('c', 'd', 11)
g.addEdge('c', 'f', 2)
g.addEdge('d', 'e', 6)
g.addEdge('e', 'f', 9)


# for v in g:
#     for w in v.getEdges():
#         print '( %s , %s, %3d)'  % ( v.id, w.id, v.getWeight(w))

Gdfs = DFSGraph()

Gdfs.addVertex('milk')
Gdfs.addVertex('egg')
Gdfs.addVertex('oil')
Gdfs.addVertex('mix')
Gdfs.addVertex('griddle')
Gdfs.addVertex('pour cup')
Gdfs.addVertex('bubbly')
Gdfs.addVertex('eat')
Gdfs.addVertex('syrup')

Gdfs.addEdge('milk', 'mix')  
Gdfs.addEdge('egg', 'mix')
Gdfs.addEdge('oil', 'mix')
Gdfs.addEdge('mix', 'syrup')
Gdfs.addEdge('griddle', 'pour cup')
Gdfs.addEdge('pour cup', 'bubbly')
Gdfs.addEdge('bubbly', 'eat')
Gdfs.addEdge('mix', 'pour cup')
Gdfs.addEdge('syrup', 'eat')

Gdfs.dfs()

vertexA = Gdfs.getVertex('a')

topSrt = Gdfs.topologicalSort()

for vertex in Gdfs.__iter__():
    oldAdjacent = vertex.getAdjacent()
    vertex.adjacent = {}            
    print vertex.id, [adj.id for adj in oldAdjacent]

Gdfs.transpose()
for vertex in Gdfs.__iter__():
    oldAdjacent = vertex.getAdjacent()
    vertex.adjacent = {}            
    print vertex.id, [adj.id for adj in oldAdjacent]