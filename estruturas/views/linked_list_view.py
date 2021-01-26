from tkinter import *
import pandas as pd
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

        
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
        #self.listWindow = Toplevel(bg="white")

        self.listContainer = Frame(master, padx=10)
        self.title = Label(master, text="Lista Encadeada", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(master, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.listContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.listContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja inserir?", fg="midnight blue") #fg = foreground = cor do label
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

root = Tk()
root["bg"] = "white" #bg=background

#Width x Height + Left + Top
#root.geometry("500x700")#tamanho e posição da tela
LinkedListView(root)

root.mainloop()




        
