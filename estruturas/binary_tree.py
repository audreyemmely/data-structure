import pandas as pd
csvData = pd.read_csv('dados/USvideos.csv', encoding = "UTF-8")

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insertNode(self, data, index):

        if self.data[index]:
            if data[index] < self.data[index]:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data, index)
            elif data[index] > self.data[index]:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data, index)
        else:
            self.data = data


    def showTree(self): #Em ordem
        if self.left:
            self.left.showTree()
        print( self.data),
        print("\n")
        if self.right:
            self.right.showTree()
    
    
    def findsuccessor(self, currentNode):
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

#-------------------MAIN-----------------------------
def insertLoop(root, data, index):
    print("Quantos dados do arquivo você deseja inserir(0 a 100)?")
    option = int(input("\nDigite aqui: "))
    i = 1
    while(i < option):
        root.insertNode(data.iloc[i], index)
        i+=1
    print(option,"itens foram inseridos na lista.\n")


def treeMenu(csvData):    

    data = csvData.sample(100)
    root = Node(data.iloc[0])
    viewsIndex = 7
    likesIndex = 8
    commentsIndex = 10


    while(True):
        print("---Menu da Árvore---")
        print("1 - Inserir por Likes")
        print("2 - Inserir por Views")
        print("3 - Inserir por Comentários")
        print("4 - Deletar por Likes ")
        print("5 - Deletar por Views")
        print("6 - Deletar por Comentários")
        print("7 - Visualizar a Árvore")
        print("8 - Sair")

        option = int(input("\nDigite a sua escolha: "))
        
        if(option == 1):
            insertLoop(root, data, likesIndex)
        elif(option == 2):
            insertLoop(root, data, viewsIndex)
        elif(option == 3):
            insertLoop(root, data, commentsIndex)
        elif(option == 4):
            print("Deletar por Likes")
            print("Digite o valor a ser deletado:")
            nodeToDelete = int(input("\nDigite aqui: "))
            root.deleteNode(root, nodeToDelete, likesIndex)
        elif(option == 5):
            print("Deletar por Views")
            print("Digite o valor ser deletado:")
            nodeToDelete = int(input("\nDigite aqui: "))
            root.deleteNode(root, nodeToDelete, viewsIndex)
        elif(option == 6):
            print("Deletar por Quantidade de Comentários")
            print("Digite o valor a ser deletado:")
            nodeToDelete = int(input("\nDigite aqui: "))
            root.deleteNode(root, nodeToDelete, commentsIndex)
        elif(option == 7):
            root.showTree()
        elif(option == 8):
            print("Saindo do Menu...\n")
            break
        else:
            print("Tem 8 opções, escolha uma\n")
    

treeMenu(csvData)

