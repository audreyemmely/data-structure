import pandas as pd
from tkinter import *
csvGraphData = pd.read_csv('dados/hero-network.csv', encoding = "UTF-8")

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
    
    def printGraph(self, dataList):
        dataList.insert(END, "---------------------------------------------------------------------------------------------")
        dataList.insert(END, "Herói -> [Conexões]")
        for vertex in self.vertices:
            print(vertex)
            dataList.insert(END, vertex)

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

def dijkstra(graph, origin, dest, msg, dataList):# vai calcular a menor distância possivel do vértice de origem para qualquer outro vértice do grafo(se houver um caminho entre eles)
    originVertex = graph.search(origin)
    if(originVertex == None):
        msg["text"] = "O vértice de origem não está no grafo"
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
    showPath(graph, origin, dest, msg, dataList)

def showPath(graph ,origin, dest, msg, dataList):
    vertex = graph.search(dest)
    if(vertex != None):
        if(vertex.previous == -1):
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
            dataList.insert(END, "Não há um caminho entre ["+origin+"] e ["+dest+"]")
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
        else:
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
            dataList.insert(END, "A distância de ["+origin+"] até ["+dest+"] é de: ")
            dataList.insert(END, str(vertex.minDistance)+"aresta(s)")
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
          
            dataList.insert(END, "Caminho do destino até a origem:")
            dataList.insert(END, vertex.hero)
            
            while vertex.previous != -1:
                dataList.insert(END, vertex.previous)
                vertex = graph.search(vertex.previous)
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
    else:
        msg["text"] = "O vértice de destino não está no grafo"


class GraphView:
    def __init__(self, master=None):
        self.graph = Graph()
        #self.listWindow = Toplevel(bg="white")

        self.graphContainer = Frame(master, padx=10)
        self.title = Label(master, text="Grafo", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(master, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.graphContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.graphContainer, padx=10)
        text = Label(insertContainer, text="Quantos vértices serão adicionados?", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.insertBox = Entry(insertContainer, width=20)
        insertButton = Button(insertContainer,width=15, text="Inserir", bg="midnight blue", fg="white", command=self.saveInsertValue)

        insertContainer.pack(pady=10) #pady = padding vertical
        text.pack(pady=10)
        self.insertBox.pack(pady=10)
        insertButton.pack(pady=10)
    
    def createVertex(self, connection):#cria um vértice para a conexão, caso ele não esteja no grafo
        searchVertex = self.graph.search(connection)#verifica se a conexão que queremos adicionar já é um vértice do grafo
        if(searchVertex == None):#caso não seja, adicionamos ele como um novo vértice do grafo
            vertex = Vertex(connection)
            self.graph.vertices.append(vertex)

    def saveInsertValue(self):
        insertValue = int(self.insertBox.get()) 
        i = 0
        while i < insertValue:
            data = csvGraphData.iloc[i]#vai pegando linha por linha em ordem do arquivo 
            #data[0] = Herói / data[1] = Conexão
            searchVertex = self.graph.search(data[0])
            if(searchVertex != None):# se o vértice já existe no grafo, adiciona só sua conexão
                searchVertex.connections.append(data[1])
                self.createVertex(data[1])
            else:# caso contrário cria o novo vértice
                vertex = Vertex(data[0])
                vertex.connections.append(data[1])
                self.graph.vertices.append(vertex)#adiciona ao grafo
                self.createVertex(data[1])
            i+=1   
         
        self.graph.printGraph(self.dataList)
        self.msg["text"] = str(insertValue)+" vértices foram inseridos no grafo."  
    
    def viewOption(self):
        viewContainer = Frame(self.graphContainer, padx=10)
        text = Label(viewContainer, text="Digite origem e destino do grafo:", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.originBox = Entry(viewContainer, width=30)
        self.destBox = Entry(viewContainer, width=30)
        viewButton = Button(viewContainer,width=15, text="Calcular Caminho", bg="midnight blue", fg="white", command=self.showViewData)
        yscrollbar = Scrollbar(viewContainer, orient="vertical")
        xscrollbar = Scrollbar(viewContainer, orient="horizontal")
        self.dataList = Listbox(viewContainer, width=60, height=15)
        self.dataList["font"] = ("Verdana", "8", "bold")
        yscrollbar["command"] = self.dataList.yview
        xscrollbar["command"] = self.dataList.xview
        self.dataList["yscrollcommand"] = yscrollbar.set

        text.pack(pady=10)
        self.originBox.pack(pady=10)
        self.destBox.pack(pady=10)
        yscrollbar.pack(side=RIGHT)
        xscrollbar.pack(side=BOTTOM)
        self.dataList.pack(side=RIGHT, pady=10)
        viewContainer.pack(pady=10)
        viewButton.pack(side=LEFT,pady=10, padx=10)
 
    
    def showViewData(self):
        if(len(self.graph.vertices) == 0):
            self.msg["text"] = "O grafo está vazio."
        else:
            if(self.originBox.get() != '' and self.destBox.get() != ''):
               dijkstra(self.graph, self.originBox.get(), self.destBox.get(), self.msg, self.dataList)
               #self.dataList.delete(0, END)#deletando todos o itens que estavam na lista
            else:
               self.msg["text"] = "Origem e destino não foram definidos." 


root = Tk()
root["bg"] = "white" #bg=background

GraphView(root)

root.mainloop()   