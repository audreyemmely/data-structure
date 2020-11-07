import pandas as pd
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertByLikes(self, data):

        if self.data[8]:
            if data[8] < self.data[8]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByLikes(data)
            elif data[8] > self.data[8]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByLikes(data)
        else:
            self.data = data

    def insertByTitle(self, data):

        if self.data[2]:
            if data[2] < self.data[2]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByTitle(data)
            elif data[2] > self.data[2]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByTitle(data)
        else:
            self.data = data

    def insertByViews(self, data):

        if self.data[7]:
            if data[7] < self.data[7]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertByViews(data)
            elif data[7] > self.data[7]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertByViews(data)
        else:
            self.data = data

    def showTree(self): #Em ordem
        if self.left:
            self.left.showTree()
        print( self.data),
        print("\n")
        if self.right:
            self.right.showTree()

#-------------------MAIN-----------------------------
def insertLoop(data, insertOption):
    print("Quantos dados do arquivo você deseja inserir(0 a 100)?")
    option = int(input("\nDigite aqui: "))
    i = 1
    while(i < option):
        insertOption(data.iloc[i])
        i+=1
    print(option,"itens foram inseridos na lista.\n")


def treeMenu(csvData):    

    data = csvData.sample(100)
    root = Node(data.iloc[0])

    while(True):
        print("---Menu da Árvore---")
        print("1 - Inserir por Likes")
        print("2 - Inserir por Views")
        print("3 - Inserir por Título")
        print("4 - Deletar por Likes ")
        print("5 - Deletar por Views")
        print("6 - Deletar por Título")
        print("7 - Visualizar a Árvore")
        print("8 - Sair")

        option = int(input("\nDigite a sua escolha: "))
        
        if(option == 1):
            insertLoop(data, lambda x: root.insertByLikes(x)) #(lambda argumento: expressão), é uma maneira de passar um função como argumento para outra função
        elif(option == 2):
            insertLoop(data, lambda x: root.insertByViews(x))
        elif(option == 3):
            insertLoop(data, lambda x: root.insertByTitle(x))
        elif(option == 4):
            print("Deletar por Likes")
        elif(option == 5):
            print("Deletar por Views")
        elif(option == 6):
            print("Deletar por Título")
        elif(option == 7):
            root.showTree()
        elif(option == 8):
            print("Saindo do Menu...\n")
            break
        else:
            print("Tem 8 opções, escolha uma\n")
    

treeMenu(csvData)

# Falta: Organizar menu, Funções delete
