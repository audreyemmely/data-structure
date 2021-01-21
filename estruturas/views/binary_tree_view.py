from tkinter import *
import pandas as pd
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertNode(self, data, index):

        if self.data[index]:
            #o nodo deve ser inserido na subárvore esquerda
            if data[index] < self.data[index]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data, index)
            #o nodo deve ser inserido na subárvore direita
            elif data[index] > self.data[index]:
                if self.right == None:
                    self.right = Node(data)
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
        dataList.insert(END, "--------------------------------")
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
               currentNode.right = self.deleteNode(currentNode.right, int(aux), index)
        return currentNode


class BinaryTreeView:
    def __init__(self, master=None):
        self.data = csvData.sample(100)
        self.root = Node(self.data.iloc[0])

        #self.treeWindow = Toplevel(bg="white")

        self.treeContainer = Frame(master, padx=10)
        self.title = Label(master, text="Árvore Binária", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(master, text="", bg="white")
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

root = Tk()
root["bg"] = "white" #bg=background
#root["background"] = "black"

#Width x Height + Left + Top
#root.geometry("500x700")#tamanho e posição da tela
#listMenu(csvData, root)
BinaryTreeView(root)

root.mainloop()

