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
def searchMinDistance(vertices):
    i = 0
    smallest = 200000 #valor aleatório, só para ter algo para comparar no primeiro loop do for
    aux = None
    for vertex in vertices:
        if(vertex.minDistance < smallest and vertex.visited == False and vertex.minDistance > -1):
            smallest = vertex.minDistance
            aux = vertex
        i+=1

    return aux

def dijkstra(graph, origin, dest):# vai calcular a menor distância possivel do vértice de origem para qualquer outro vértice do grafo
    originVertex = graph.search(origin)
    if(originVertex == None):
        print("O vértice de origem não está no grafo.")
        return
    else:
        originVertex.minDistance = 0
    i = 0
    while i < len(graph.vertices):# no primeiro loop da busca, sempre irá pegar o vértice de origem, pois ele o único com minDistance != -1
        currentVertex = searchMinDistance(graph.vertices)#vai retornar o vértice com menor distância e que ainda não foi visitado
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
        
        

def createGraph(graph):
    option1 = int(input("Quantos vértices serão adicionados? "))
    i = 0
    while i < option1:
        vertex = input("Digite o vértice:")
        vtx = graph.search(vertex)#procura pra ver se já existe o vértice no grafo
        if(vtx == None):#caso ele não exista, cria um novo vértice
            vtx = Vertex(vertex)
            graph.vertices.append(vtx)#adiciona o novo vértice a lista de vértices do grafo
        j = 0
        option2 = int(input("Quantas conexões serão adicionadas ao vértice? "))
        while j < option2:
            connection = input("Digite a conexão:")
            vtx.connections.append(connection)#adiciona uma nova conexão ao vértice
            if(graph.search(connection) == None):
                graph.vertices.append(Vertex(connection))# já adiciona a nova conexão como um vértice no grafo
            j+=1
    
        i+=1
#--------------------------------------------------------------
graph = Graph()
createGraph(graph)

origin = input("Vértice de origem:")
dest = input("Vértice de destino:")

dijkstra(graph, origin, dest)
graph.printGraph()

for x in graph.vertices:
    print(x.hero, " distance-> " , x.minDistance, " previous -> ", x.previous)


#Utilizei esse grafo(não direcionado) abaixo para testar:

# A -> [B,D]
# B -> [A,C,D,E]
# C -> [B,E]
# D -> [A,B,E,F]
# E -> [B,C,D,F]
# F -> [E,D]