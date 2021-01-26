#importando a biblioteca pandas, responsável pela leitura do arquivo csv
from tkinter import *
import pandas as pd
#lendo o arquivo csv e armazenando na variável 'data'
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

#a classe Elemento é utilizada na função 'empilhar', para criar a pilha, definindo o atual conteúdo e o próximo
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
        #self.listWindow = Toplevel(bg="white")

        self.stackContainer = Frame(master, padx=10)
        self.title = Label(master, text="Pilha", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.msg = Label(master, text="", bg="white")
        self.msg["font"] = ("Verdana", "12", "bold")

        self.title.pack(pady=10)
        self.stackContainer.pack(pady=20)
        self.msg.pack(side=BOTTOM)

        self.insertOption()
        self.deleteOption()
        self.viewOption()
        

    def insertOption(self):
        insertContainer = Frame(self.stackContainer, padx=10)
        text = Label(insertContainer, text="Quantos dados do arquivo você deseja empilhar?", fg="midnight blue") #fg = foreground = cor do label
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


root = Tk()
root["bg"] = "white" #bg=background

StackView(root)

root.mainloop()