import csv
from csv_model import CsvModel
from linked_list import LinkedList

def listMenu(csvData):
    list = LinkedList()
    while(True):
        print("---Menu da Lista---")
        print("1 - Inserir")
        print("2 - Visualizar")
        print("3 - Deletar ")
        print("4 - Sair")

        option = int(input("\nDigite a sua escolha: "))
        
        # No inserir eu não sei se é para inserir um novo item a uma lista já criada, ou apenas pegar os dados do arquivo csv e colocar na lista
        if(option == 1):
            print("Quantos dados do arquivo você deseja inserir?")
            insertOption = int(input("\nDigite aqui: "))
            i = 1
            for row in csvData:
                data = CsvModel(row)
                list.insertAtBeginning(data)
                if( i == insertOption):
                    break
                i+= 1
        elif(option == 2):
            if(list.isEmpty()):
                print("A lista está vazia.\n")
            else:
                list.showList()
        elif (option == 3):
            if(list.isEmpty()):
                print("A lista está vazia.\n")
            else:
                deleteOption = input("\nDigite o titulo que será deletado: ")
                print(list.delete(deleteOption))
        elif (option == 4):
            print("Saindo do Menu\n")
            break
        else:
            print("Tem 4 opções, escolha uma\n")



with open('../dados/USvideos.csv', 'r') as csvFile:
    csvData = csv.reader(csvFile, delimiter = ',')
    csvData.__next__()

    while(True):
        print("1 - Lista")
        print("2 - Pilha")
        print("3 - Sair")

        option = int(input("\nDigite a sua escolha: "))

        if(option == 1):
            listMenu(csvData)
        elif(option == 2):
            print("......")
        elif(option == 3):
            print("Saindo do programa")
            break
        else:
            print("Digite certo ai, na moral")

    
