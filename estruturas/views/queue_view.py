import pandas as pd
from tkinter import *
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

# criando os nós da fila
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
        #self.listWindow = Toplevel(bg="white")

        self.queueContainer = Frame(master, padx=10)
        self.title = Label(master, text="Fila", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(master, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.queueContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.queueContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja enfileirar?", fg="midnight blue") #fg = foreground = cor do label
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



root = Tk()
root["bg"] = "white" #bg=background

QueueView(root)

root.mainloop()
