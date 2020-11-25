import pandas as pd
csvData = pd.read_csv('dados/hero-network.csv', encoding = "UTF-8")

class Vertex:
    
    def __init__(self, hero):
        self.hero = hero
        self.connections = []
    
    def addConec(self, connection):
        self.connections.append(connection)

    def __str__(self):
        return self.hero+" -> %s" %self.connections

class Graph:

    def __init__(self):
        self.vertices = []
    
    def search(self, hero):
        for vertex in self.vertices:
            if(hero == vertex.hero):
                return vertex
        return None
    
    def printGraph(self):
        print('\n')
        print("Herói -> [Conexões]")
        for vertex in self.vertices:
            print(vertex)

#--------------------MAIN------------------------
graph = Graph()
option = int(input("Quantos vértices serão adcionados? "))
i = 0
while i < option:
    data = csvData.iloc[i]
    #data[0] = herói / data[1] = Conexão
    searchVertex = graph.search(data[0])
    if(searchVertex != None):
        searchVertex.addConec(data[1])
    else:
        vertex = Vertex(data[0])
        vertex.connections.append(data[1])
        graph.vertices.append(vertex)
    i+=1

graph.printGraph()