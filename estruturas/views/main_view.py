from tkinter import *
import pandas as pd
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")
csvGraphData = pd.read_csv('dados/hero-network.csv', encoding = "UTF-8")

#------------------------------------------------LinkedList-----------------------------------       
class Node:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.nextNode = None

class LinkedList:
    def __init__(self, master=None):
        self.head = None    

    def isEmpty(self):
        if(self.head == None):
            return True
        else:
            return False
    
    def insertAtBeginning(self, nodeValue):
        newNode = Node(nodeValue)
        newNode.nextNode = self.head
        self.head = newNode

    def showList(self, dataList):
        aux = self.head
        while aux != None:
            dataList.insert(END, "Video Id: "+aux.nodeValue[0])
            dataList.insert(END, "Title: "+aux.nodeValue[2])
            dataList.insert(END, "Channel Title: "+aux.nodeValue[3])
            dataList.insert(END, "Publish Time: "+aux.nodeValue[5])
            dataList.insert(END, "Views: "+str(aux.nodeValue[7]))
            dataList.insert(END, "Likes: "+str(aux.nodeValue[8]))
            dataList.insert(END, "Dislikes: "+str(aux.nodeValue[9]))
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
            
            aux = aux.nextNode
    
    def delete(self, video_id):
        #nodeValue[0] retorna o valor do video_id do item da lista
        if(self.head.nodeValue[0].lower() == video_id.lower()):
            self.head = self.head.nextNode
            return video_id +" foi deletado.\n"
        else:
            aux = self.head
            previous = None
            while (aux.nextNode != None):
                previous = aux
                aux = aux.nextNode
                if(aux.nodeValue[0].lower() == video_id.lower() and aux.nextNode != None):
                    previous.nextNode = aux.nextNode
                    return video_id +" foi deletado.\n"
                elif(aux.nodeValue[0].lower() == video_id.lower() and aux.nextNode == None):
                    previous.nextNode = None
                    return video_id +" foi deletado.\n"
            return video_id +" não está na lista.\n"

class LinkedListView:
    def __init__(self, master=None):
        self.linkedList = LinkedList()
        self.listWindow = Toplevel(bg="white")

        self.listContainer = Frame(self.listWindow, padx=10)
        self.title = Label(self.listWindow, text="Lista Encadeada", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(self.listWindow, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.listContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.listContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja inserir?(0 a 100)", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.insertBox = Entry(insertContainer, width=20)
        insertButton = Button(insertContainer,width=15, text="Inserir", bg="midnight blue", fg="white", command=self.saveInsertValue)

        insertContainer.pack(pady=10) #pady = padding vertical
        text.pack(pady=10)
        self.insertBox.pack(pady=10)
        insertButton.pack(pady=10)

    def saveInsertValue(self):
        insertValue = int(self.insertBox.get()) 
        data = csvData.sample(100)
        i=0
        while(i < insertValue):
            self.linkedList.insertAtBeginning(data.iloc[i])
            i+=1
        self.msg["text"] = str(insertValue)+" itens foram inseridos na lista."       
    
    def viewOption(self):
        viewContainer = Frame(self.listContainer, padx=10)
        viewButton = Button(viewContainer,width=15, text="Visualizar", bg="midnight blue", fg="white", command=self.showViewData)
        yscrollbar = Scrollbar(viewContainer, orient="vertical")
        xscrollbar = Scrollbar(viewContainer, orient="horizontal")
        self.dataList = Listbox(viewContainer, width=60, height=15)
        self.dataList["font"] = ("Verdana", "8", "bold")
        yscrollbar["command"] = self.dataList.yview
        xscrollbar["command"] = self.dataList.xview
        self.dataList["yscrollcommand"] = yscrollbar.set

        
        yscrollbar.pack(side=RIGHT)
        xscrollbar.pack(side=BOTTOM)
        self.dataList.pack(side=RIGHT, pady=10)
        viewContainer.pack(pady=10)
        viewButton.pack(side=LEFT,pady=10, padx=10)
    
    def showViewData(self):
        self.dataList.delete(0, END)#deletando todos o itens que estavam na lista
        if(self.linkedList.isEmpty()):
            self.msg["text"] = "A lista está vazia."
        else:
            self.linkedList.showList(self.dataList)

    def deleteOption(self):
        deleteContainer = Frame(self.listContainer, width=250)
        text = Label(deleteContainer, text="Digite o ID do video que você deseja deletar:", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.deleteBox = Entry(deleteContainer, width=20)
        deleteButton = Button(deleteContainer,width=15, text="Deletar", bg="midnight blue", fg="white", command=self.saveDeleteValue)
        deleteContainer.pack(pady=10)
        text.pack(pady=10)
        self.deleteBox.pack(pady=10)
        deleteButton.pack(pady=10)
        
    def saveDeleteValue(self):
        if(self.linkedList.isEmpty()):
            self.msg["text"] = "A lista está vazia."
        else:
            deleteValue = self.deleteBox.get()
            self.msg["text"] = self.linkedList.delete(deleteValue)

#----------------------------------------------Pilha--------------------------------------------------------------
class Elemento: 
  def __init__(self, c, p):
    self.conteudo = c
    self.proximo = p

class Pilha:
  #a função '__init__' inicia a pilha com o topo vazio
  def __init__(self):
    self.topo = None
    
  #a função 'vazia' checa se uma pilha está vazia ou não
  def vazia(self): 
    if self.topo == None:
      return True
    else:
      return False
    
  #a função 'empilhar' insere o conteúdo no topo da pilha
  def empilhar(self, novo_conteudo): 
      novo_elemento = Elemento(novo_conteudo, self.topo)
      self.topo = novo_elemento
  
  #a função 'desempilhar' retira da pilha o último item que foi adicionado (o item que está no topo)
  def desempilhar(self):
    elemento_excluido = self.topo
    self.topo = self.topo.proximo
    del elemento_excluido
  
    
  #a função 'listar' retorna todos elementos existentes na pilha, se não estiver vazia. Se estiver vazia, ela retorna 'A pilha está vazia'
  def listar(self, dataList):
    ver_conteudo = self.topo
    while ver_conteudo != None:
        dataList.insert(END, "Video Id: "+ver_conteudo.conteudo[0])
        dataList.insert(END, "Title: "+ver_conteudo.conteudo[2])
        dataList.insert(END, "Channel Title: "+ver_conteudo.conteudo[3])
        dataList.insert(END, "Publish Time: "+ver_conteudo.conteudo[5])
        dataList.insert(END, "Views: "+str(ver_conteudo.conteudo[7]))
        dataList.insert(END, "Likes: "+str(ver_conteudo.conteudo[8]))
        dataList.insert(END, "Dislikes: "+str(ver_conteudo.conteudo[9]))
        dataList.insert(END, "---------------------------------------------------------------------------------------------")

        ver_conteudo = ver_conteudo.proximo

class StackView:
    def __init__(self, master=None):
        self.stack = Pilha()
        self.listWindow = Toplevel(bg="white")

        self.stackContainer = Frame(self.listWindow, padx=10)
        self.title = Label(self.listWindow, text="Pilha", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(self.listWindow, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.stackContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.stackContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja empilhar?(0 a 100)", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.insertBox = Entry(insertContainer, width=20)
        insertButton = Button(insertContainer,width=15, text="Empilhar", bg="midnight blue", fg="white", command=self.saveInsertValue)

        insertContainer.pack(pady=10) #pady = padding vertical
        text.pack(pady=10)
        self.insertBox.pack(pady=10)
        insertButton.pack(pady=10)

    def saveInsertValue(self):
        insertValue = int(self.insertBox.get()) 
        data = csvData.sample(100)
        i=0
        while(i < insertValue):
            self.stack.empilhar(data.iloc[i])
            i+=1
        self.msg["text"] = str(insertValue)+" itens foram empilhados."       
    
    def viewOption(self):
        viewContainer = Frame(self.stackContainer, padx=10)
        viewButton = Button(viewContainer,width=15, text="Visualizar", bg="midnight blue", fg="white", command=self.showViewData)
        yscrollbar = Scrollbar(viewContainer, orient="vertical")
        xscrollbar = Scrollbar(viewContainer, orient="horizontal")
        self.dataList = Listbox(viewContainer, width=60, height=15)
        self.dataList["font"] = ("Verdana", "8", "bold")
        yscrollbar["command"] = self.dataList.yview
        xscrollbar["command"] = self.dataList.xview
        self.dataList["yscrollcommand"] = yscrollbar.set

        
        yscrollbar.pack(side=RIGHT)
        xscrollbar.pack(side=BOTTOM)
        self.dataList.pack(side=RIGHT, pady=10)
        viewContainer.pack(pady=10)
        viewButton.pack(side=LEFT,pady=10, padx=10)
    
    def showViewData(self):
        self.dataList.delete(0, END)#deletando todos o itens que estavam na lista
        if(self.stack.vazia()):
            self.msg["text"] = "A pilha está vazia."
        else:
            self.stack.listar(self.dataList)

    def deleteOption(self):
        deleteContainer = Frame(self.stackContainer, width=250)
        text = Label(deleteContainer, text="Desempilhar", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        #self.deleteBox = Entry(deleteContainer, width=20)
        popButton = Button(deleteContainer,width=15, text="Desempilhar", bg="midnight blue", fg="white", command=self.saveDeleteValue)
        deleteContainer.pack(pady=10)
        #text.pack(pady=10)
        #self.deleteBox.pack(pady=10)
        popButton.pack(pady=10)
        
    def saveDeleteValue(self):
        if(self.stack.vazia()):
            self.msg["text"] = "A Pilha está vazia."
        else:
            self.stack.desempilhar()
            self.msg["text"] = "Item desempilhado"
#----------------------------------------------Queue-------------------------------------------------------------
class queueNode: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self): 
        if self.head == None:
            return True
        else:
            return False
    
    # Inserindo um elemento por vez
    def enqueue(self, newNode):
        newContent = queueNode(newNode)
        newContent.next = None
        if self.head == None:
            self.head = newContent 
        else:
            last = self.head
            while last.next: 
                last = last.next
            last.next = newContent

    # Removendo um elemento por vez
    def dequeue(self):
        deletedItem = self.head
        self.head = self.head.next
        del deletedItem

    def showQueue(self, dataList):
        showContent = self.head
        while showContent != None:
            dataList.insert(END, "Video Id: "+showContent.value[0])
            dataList.insert(END, "Title: "+showContent.value[2])
            dataList.insert(END, "Channel Title: "+showContent.value[3])
            dataList.insert(END, "Publish Time: "+showContent.value[5])
            dataList.insert(END, "Views: "+str(showContent.value[7]))
            dataList.insert(END, "Likes: "+str(showContent.value[8]))
            dataList.insert(END, "Dislikes: "+str(showContent.value[9]))
            dataList.insert(END, "---------------------------------------------------------------------------------------------")
            
            showContent = showContent.next
    
class QueueView:
    def __init__(self, master=None):
        self.queue = Queue()
        self.listWindow = Toplevel(bg="white")

        self.queueContainer = Frame(self.listWindow, padx=10)
        self.title = Label(self.listWindow, text="Fila", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(self.listWindow, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.queueContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.queueContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja enfileirar?(0 a 100)", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.insertBox = Entry(insertContainer, width=20)
        insertButton = Button(insertContainer,width=15, text="Enfileirar", bg="midnight blue", fg="white", command=self.saveInsertValue)

        insertContainer.pack(pady=10) #pady = padding vertical
        text.pack(pady=10)
        self.insertBox.pack(pady=10)
        insertButton.pack(pady=10)

    def saveInsertValue(self):
        insertValue = int(self.insertBox.get()) 
        data = csvData.sample(100)
        i=0
        while(i < insertValue):
            self.queue.enqueue(data.iloc[i])
            i+=1
        self.msg["text"] = str(insertValue)+" itens foram enfileirados."       
    
    def viewOption(self):
        viewContainer = Frame(self.queueContainer, padx=10)
        viewButton = Button(viewContainer,width=15, text="Visualizar", bg="midnight blue", fg="white", command=self.showViewData)
        yscrollbar = Scrollbar(viewContainer, orient="vertical")
        xscrollbar = Scrollbar(viewContainer, orient="horizontal")
        self.dataList = Listbox(viewContainer, width=60, height=15)
        self.dataList["font"] = ("Verdana", "8", "bold")
        yscrollbar["command"] = self.dataList.yview
        xscrollbar["command"] = self.dataList.xview
        self.dataList["yscrollcommand"] = yscrollbar.set

        
        yscrollbar.pack(side=RIGHT)
        xscrollbar.pack(side=BOTTOM)
        self.dataList.pack(side=RIGHT, pady=10)
        viewContainer.pack(pady=10)
        viewButton.pack(side=LEFT,pady=10, padx=10)
    
    def showViewData(self):
        self.dataList.delete(0, END)#deletando todos o itens que estavam na lista
        if(self.queue.isEmpty()):
            self.msg["text"] = "A fila está vazia."
        else:
            self.queue.showQueue(self.dataList)

    def deleteOption(self):
        deleteContainer = Frame(self.queueContainer, width=250)
        text = Label(deleteContainer, text="Desenfileirar", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        dequeueButton = Button(deleteContainer,width=15, text="Desenfileirar", bg="midnight blue", fg="white", command=self.saveDeleteValue)
        deleteContainer.pack(pady=10)
        dequeueButton.pack(pady=10)
        
    def saveDeleteValue(self):
        if(self.queue.isEmpty()):
            self.msg["text"] = "A fila está vazia."
        else:
            self.queue.dequeue()
            self.msg["text"] = "Item desenfileirado"

#----------------------------------------------BinaryTree--------------------------------------------------------
class TreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertNode(self, data, index):

        if self.data[index]:
            #o nodo deve ser inserido na subárvore esquerda
            if data[index] < self.data[index]:
                if self.left == None:
                    self.left = TreeNode(data)
                else:
                    self.left.insertNode(data, index)
            #o nodo deve ser inserido na subárvore direita
            elif data[index] > self.data[index]:
                if self.right == None:
                    self.right = TreeNode(data)
                else:
                    self.right.insertNode(data, index)
        else:
            #o nodo deve ser inserido na raiz
            self.data = data


    def showTree(self, dataList): #Em ordem
        #percorre a subárvore da esquerda
        if self.left:
            self.left.showTree(dataList)
        #visita a raiz
        dataList.insert(END, "Video Id: "+self.data[0])
        dataList.insert(END, "Title: "+self.data[2])
        dataList.insert(END, "Channel Title: "+self.data[3])
        dataList.insert(END, "Publish Time: "+self.data[5])
        dataList.insert(END, "Views: "+str(self.data[7]))
        dataList.insert(END, "Likes: "+str(self.data[8]))
        dataList.insert(END, "Dislikes: "+str(self.data[9]))
        dataList.insert(END, "Comment Count: "+str(self.data[10]))
        dataList.insert(END, "---------------------------------------------------------------------------------------------")
        #print(self.data),
        #print("\n")
        #percorre a subárvore da direita
        if self.right:
            self.right.showTree(dataList)
    
    
    def findsuccessor(self, currentNode):
        #quando sair do while, "currentNode" será o nó mais à esquerda da subárvore à direita
        while currentNode.left != None:
            currentNode = currentNode.left
        return currentNode.data
    
    def deleteNode(self, currentNode, nodeToDelete, index):
        if currentNode == None:
            return currentNode
        if(nodeToDelete < int(currentNode.data[index])):
            currentNode.left = self.deleteNode(currentNode.left, nodeToDelete, index)
        elif(nodeToDelete > int(currentNode.data[index])):
            currentNode.right = self.deleteNode(currentNode.right, nodeToDelete, index)
        else:
            if currentNode.left == None:
                currentNode = currentNode.right
            elif currentNode.right == None:
                currentNode = currentNode.left
            else:
               aux = self.findsuccessor(currentNode.right)
               currentNode.data = aux
               currentNode.right = self.deleteNode(currentNode.right, aux, index)
        return currentNode


class BinaryTreeView:
    def __init__(self, master=None):
        self.data = csvData.sample(100)
        self.root = TreeNode(self.data.iloc[0])

        self.treeWindow = Toplevel(bg="white")

        self.treeContainer = Frame(self.treeWindow, padx=10)
        self.title = Label(self.treeWindow, text="Árvore Binária", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(self.treeWindow, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.treeContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.treeContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja inserir? (0 a 100)", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.insertBox = Entry(insertContainer, width=20)
        likesButton = Button(insertContainer,width=18, text="Inserir por Likes", bg="midnight blue", fg="white", command=self.insertLikes)
        viewsButton = Button(insertContainer,width=18, text="Inserir por Views", bg="midnight blue", fg="white", command=self.insertViews)
        commentsButton = Button(insertContainer,width=18, text="Inserir por Comentários", bg="midnight blue", fg="white", command=self.insertComments)

        insertContainer.pack(pady=10) #pady = padding vertical
        text.pack(pady=10)
        self.insertBox.pack(pady=10)
        likesButton.pack(side=LEFT, pady=10, padx=5)
        viewsButton.pack(side=RIGHT, pady=10, padx=5)
        commentsButton.pack(side=RIGHT, pady=10, padx=5)

    def insertViews(self):
        self.saveInsertValue(7)
    def insertLikes(self):
        self.saveInsertValue(8)
    def insertComments(self):
        self.saveInsertValue(10)

    def saveInsertValue(self, index):
        insertValue = int(self.insertBox.get()) 
        i = 1
        while(i < insertValue):
            self.root.insertNode(self.data.iloc[i], index)
            i+=1
        self.msg["text"] = str(insertValue)+" itens foram inseridos na Árvore."      
    
    def viewOption(self):
        viewContainer = Frame(self.treeContainer, padx=10)
        viewButton = Button(viewContainer,width=15, text="Visualizar", bg="midnight blue", fg="white", command=self.showViewData)
        yscrollbar = Scrollbar(viewContainer, orient="vertical")
        xscrollbar = Scrollbar(viewContainer, orient="horizontal")
        self.dataList = Listbox(viewContainer, width=60, height=15)
        self.dataList["font"] = ("Verdana", "8", "bold")
        yscrollbar["command"] = self.dataList.yview
        xscrollbar["command"] = self.dataList.xview
        self.dataList["yscrollcommand"] = yscrollbar.set

        
        yscrollbar.pack(side=RIGHT)
        xscrollbar.pack(side=BOTTOM)
        self.dataList.pack(side=RIGHT, pady=10)
        viewContainer.pack(pady=10)
        viewButton.pack(side=LEFT,pady=10, padx=10)
    
    def showViewData(self):
        self.dataList.delete(0, END)#deletando todos o itens que estavam na lista
        self.root.showTree(self.dataList)

    def deleteOption(self):
        deleteContainer = Frame(self.treeContainer, width=250)
        text = Label(deleteContainer, text="Digite o valor do item que você deseja deletar:", fg="midnight blue") #fg = foreground = cor do label
        text["font"] = ("Verdana", "10", "bold")
        self.deleteBox = Entry(deleteContainer, width=20)
        likesButton = Button(deleteContainer,width=18, text="Deletar por Likes", bg="midnight blue", fg="white", command=self.deleteLikes)
        viewsButton = Button(deleteContainer,width=18, text="Deletar por Views", bg="midnight blue", fg="white", command=self.deleteViews)
        commentsButton = Button(deleteContainer,width=18, text="Deletar por Comentários", bg="midnight blue", fg="white", command=self.deleteComments)

        deleteContainer.pack(pady=10)
        text.pack(pady=10)
        self.deleteBox.pack(pady=10)
        likesButton.pack(side=LEFT, pady=10, padx=5)
        viewsButton.pack(side=RIGHT, pady=10, padx=5)
        commentsButton.pack(side=RIGHT, pady=10, padx=5)

    def deleteViews(self):
        self.saveDeleteValue(7)
    def deleteLikes(self):
        self.saveDeleteValue(8)
    def deleteComments(self):
        self.saveDeleteValue(10)
        
    def saveDeleteValue(self, index):
        deleteValue = int(self.deleteBox.get())
        #Não está deletando a raiz
        print("++++++++++++==",deleteValue)
        aux = self.root
        self.root.deleteNode(aux, deleteValue, index)

#----------------------------------------------Graph---------------------------------------------------------------
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
        self.listWindow = Toplevel(bg="white")

        self.graphContainer = Frame(self.listWindow, padx=10)
        self.title = Label(self.listWindow, text="Grafo", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(self.listWindow, text="", bg="white")
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


#----------------------------------------------Aplication--------------------------------------------------------
class Application:

    def __init__(self, master=None):
        self.master = master
        self.mainContainer = Frame(master, padx=10)
        self.title = Label(master, text="Menu", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.title.pack(pady=10)
        self.mainContainer.pack(pady=20)
        self.homeView()
        
    def homeView(self):
        self.listButton = Button(self.mainContainer, width=15, text="Lista Encadeada", bg="midnight blue", fg="white", command=LinkedListView)
        self.stackButton = Button(self.mainContainer, width=15, text="Pilha", bg="midnight blue", fg="white", command=StackView)
        self.queueButton = Button(self.mainContainer, width=15, text="Fila", bg="midnight blue", fg="white", command=QueueView)
        self.binaryTreeButton = Button(self.mainContainer, width=15, text="Árvore Binária", bg="midnight blue", fg="white", command=BinaryTreeView)
        self.graphButton = Button(self.mainContainer, width=15, text="Grafo", bg="midnight blue", fg="white", command=GraphView)
        self.exitButton = Button(self.mainContainer, width=15, text="Sair", command=self.master.quit, bg="midnight blue", fg="white")

        self.listButton.pack(pady=10) 
        self.stackButton.pack(pady=10)
        self.queueButton.pack(pady=10)
        self.binaryTreeButton.pack(pady=10)
        self.graphButton.pack(pady=10)
        self.exitButton.pack(pady=10)




root = Tk()
root["bg"] = "white" #bg=background

#Width x Height + Left + Top
#root.geometry("500x500")#tamanho e posição da tela

Application(root)
root.mainloop()



        
