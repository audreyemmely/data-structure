import pandas as pd
csvData = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

class Node:
    def __init__(self, nodeValue):
        self.nodeValue = nodeValue
        self.nextNode = None

class LinkedList:
    def __init__(self):
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

    def showList(self):
        aux = self.head
        while aux != None:
            print(aux.nodeValue)
            print("\n")
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

def listMenu(csvData):
    list = LinkedList()
    while(True):
        print("---Menu da Lista---")
        print("1 - Inserir")
        print("2 - Visualizar")
        print("3 - Deletar ")
        print("4 - Sair")

        option = int(input("\nDigite a sua escolha: "))
        
        if(option == 1):
            print("Quantos dados do arquivo você deseja inserir?")
            data = csvData.sample(100)
            insertOption = int(input("\nDigite aqui: "))
            i = 0
            while(i < insertOption):
                list.insertAtBeginning(data.iloc[i])
                i+=1
            print(insertOption,"itens foram inseridos na lista.\n")
        elif(option == 2):
            if(list.isEmpty()):
                print("A lista está vazia.\n")
            else:
                list.showList()
        elif (option == 3):
            if(list.isEmpty()):
                print("A lista está vazia.\n")
            else:
                deleteOption = input("\nDigite o ID do titulo que será deletado: ")
                print(list.delete(deleteOption))
        elif (option == 4):
            print("Saindo do Menu...\n")
            break
        else:
            print("Tem 4 opções, escolha uma\n")

listMenu(csvData)
