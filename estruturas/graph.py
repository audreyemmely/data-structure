import pandas as pd
csvData = pd.read_csv('dados/hero-network.csv', encoding = "UTF-8")

class Vertex:
    
    def __init__(self, hero):
        self.hero = hero
        self.connections = []
        self.minDistance = -1
        self.visited = False
        self.previous = -1

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
        print("-------------------")
        print("Herói -> [Conexões]")
        for vertex in self.vertices:
            print(vertex)
        print("-------------------")

#--------------------MAIN------------------------
def searchMinDistance(vertices):#vai retornar o vértice com menor distância e que ainda não foi visitado
    i = 0
    smallest = 200000 #valor aleatório, só para ter algo para comparar no primeiro loop do for
    aux = None
    for vertex in vertices:
        if(vertex.minDistance < smallest and vertex.visited == False and vertex.minDistance != -1):
            smallest = vertex.minDistance
            aux = vertex
        i+=1

    return aux

def dijkstra(graph, origin, dest):# vai calcular a menor distância possivel do vértice de origem para qualquer outro vértice do grafo(se houver um caminho entre eles)
    originVertex = graph.search(origin)
    if(originVertex == None):
        print("O vértice de origem não está no grafo.")
        return
    else:
        originVertex.minDistance = 0
    i = 0
    while i < len(graph.vertices):# no primeiro loop da busca, sempre irá pegar o vértice de origem, pois ele o único com minDistance != -1
        currentVertex = searchMinDistance(graph.vertices)
        if(currentVertex != None):
            currentVertex.visited = True

            for connecVertex in currentVertex.connections:#Verifica a distância do vértice atual com suas conexões, caso seja um valor menor ao que já estava lá, atualiza a distância e o vértice anterior
                vertex = graph.search(connecVertex)
                if(vertex.minDistance == -1):
                    vertex.minDistance = currentVertex.minDistance + 1
                    vertex.previous = currentVertex.hero
                elif(vertex.minDistance > currentVertex.minDistance + 1):
                    vertex.minDistance = currentVertex.minDistance + 1
                    vertex.previous = currentVertex.hero

            i+=1
        else:
            break
    showPath(graph, origin, dest)

def showPath(graph ,origin, dest):
    vertex = graph.search(dest)
    if(vertex.previous == -1):
        print("-------------------------------------------------")
        print("Não há um caminho entre [",origin,"] e [",dest,"]")
        print("-------------------------------------------------")
    else:
        print("-------------------------------")
        print("A distância de [",origin,"] até [",dest,"] é de:",vertex.minDistance,"aresta(s)")
        print("-------------------------------")
        print("Caminho do destino até a origem")
        print(vertex.hero)
        while vertex.previous != -1:
            print(vertex.previous)
            vertex = graph.search(vertex.previous)
        print("---------------------------------")
    

def createVertex(connection):#cria um vértice para a conexão, caso ele não esteja no grafo
    searchVertex = graph.search(connection)#verifica se a conexão que queremos adicionar já é um vértice do grafo
    if(searchVertex == None):#caso não seja, adicionamos ele como um novo vértice do grafo
        vertex = Vertex(connection)
        graph.vertices.append(vertex)

graph = Graph()
option = int(input("Quantos vértices serão adcionados? "))
i = 0
while i < option:
    data = csvData.iloc[i]#vai pegando linha por linha em ordem do arquivo 
    #data[0] = Herói / data[1] = Conexão
    searchVertex = graph.search(data[0])
    if(searchVertex != None):# se o vértice já existe no grafo, adiciona só sua conexão
        searchVertex.connections.append(data[1])
        createVertex(data[1])
    else:# caso contrário cria o novo vértice
        vertex = Vertex(data[0])
        vertex.connections.append(data[1])
        graph.vertices.append(vertex)#adiciona ao grafo
        createVertex(data[1])

        
    i+=1
graph.printGraph()
origin = input("Vértice de origem:")
dest = input("Vértice de destino:")

dijkstra(graph, origin, dest)


for x in graph.vertices:#dps apagar, só para teste
    print(x.hero, " distance-> " , x.minDistance, " previous -> ", x.previous)