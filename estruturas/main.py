from linked_list import LinkedList
import pandas as pd
csvData = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

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
    

    
