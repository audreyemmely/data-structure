# Importando a biblioteca Pandas para inserindo os dados do CSV
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

# criando os nós da fila
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self): 
        if self.head == None:
            print ("A fila está vazia\n")
        else:
            print ("A fila não está vazia\n")
    
    # REMOVENDO ELEMENTO POR ELEMENTO
    def push(self, newNode):
        newContent = Node(newNode)
        newContent.next = None
        if self.head == None:
            self.head = newContent 
            print("Elemento {} foi inserido na fila\n".format(newContent.value))
        else:
            last = self.head
            while last.next: 
                last = last.next
            last.next = newContent
            print("Elemento {} foi inserido na fila\n".format(newContent.value))

    def pop(self):
        if self.head == None:
            print("A fila está vazia\n")
        else:
            deletedItem = self.head
            self.head = self.head.next
            print("Elemento ({}) foi excluído da fila\n".format(deletedItem.value))
            del deletedItem

    def length(self):
        if (self.head == None):
            return 0
        count = 0
        content = self.head
        while content != None:
            count += 1
            content = content.next
        return count

    def showQueue(self):
        if self.head == None:
            print("A pilha está vazia\n")
        showContent = self.head
        while showContent != None:
            print(showContent.value)
            print("\n")
            showContent = showContent.next

def menu(data):
    while(True):
        myQueue = Queue()
        while(True):
            print("---Menu da Fila---")
            print("1 - Checar se está vazia ou não")
            print("2 - Adicionar à fila")
            print("3 - Remover da fila")
            print("4 - Informar tamanho da fila")
            print("5 - Listar fila")
            print("6 - Sair")

            option = int(input("\nInforme a opção: "))

            if option == 1:
                myQueue.isEmpty()
            elif option == 2: 
                content = int(input("\nDigite o elemento que você deseja inserir: "))
                data = data.sample(100)
                myQueue.push(data.iloc[content]) 
            elif option == 3:
                myQueue.pop() 
            elif option == 4:
                print("A fila contém {} elementos\n".format(myQueue.length())) 
            elif option == 5:
                myQueue.showQueue()
            elif option == 6:
                print("Até a próxima! :D\n")
                break
            else:
                print("Opção inválida, digite uma opção mostrada no menu!\n")

menu(data)