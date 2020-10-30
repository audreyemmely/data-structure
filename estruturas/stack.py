#importando a biblioteca pandas, responsável pela leitura do arquivo csv
import pandas as pd
#lendo o arquivo csv e armazenando na variável 'data'
data = pd.read_csv('https://raw.githubusercontent.com/audreyemmely/estrutura-de-dados/main/dados/USvideos.csv', encoding = "UTF-8")

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
      print ("A pilha está vazia\n")
    else:
      print ("A pilha não está vazia\n")
    
  #a função 'empilhar' insere o conteúdo no topo da pilha
  def empilhar(self, novo_conteudo): 
      novo_elemento = Elemento(novo_conteudo, self.topo)
      self.topo = novo_elemento
      print("Elemento {} foi inserido no topo da pilha\n".format(novo_elemento.conteudo))
  
  #a função 'desempilhar' retira da pilha o último item que foi adicionado (o item que está no topo)
  def desempilhar(self):
    if self.topo == None:
      print("A pilha está vazia\n")
    elemento_excluido = self.topo
    self.topo = self.topo.proximo
    print("Elemento ({}) foi excluído do topo da pilha\n".format(elemento_excluido.conteudo))
    del elemento_excluido
  
  #a função 'tamanho' retorna o tamanho total da pilha
  def tamanho(self):
    if (self.topo == None):
      return 0
    contador_pilha = 0
    conteudo_pilha = self.topo
    while conteudo_pilha != None:
      contador_pilha += 1
      conteudo_pilha = conteudo_pilha.proximo
    return contador_pilha
    
  #a função 'listar' retorna todos elementos existentes na pilha, se não estiver vazia. Se estiver vazia, ela retorna 'A pilha está vazia'
  def listar(self):
    if self.topo == None:
      print("A pilha está vazia\n")
    ver_conteudo = self.topo
    while ver_conteudo != None:
      print(ver_conteudo.conteudo)
      print("\n")
      ver_conteudo = ver_conteudo.proximo

#a função 'stackMenu' recebe os dados armazenados na variável 'data', cria a pilha 'minha_pilha', e executa as funções que foram criadas acima
def stackMenu(data):
      minha_pilha = Pilha()
      while(True):
          print("---Menu da Pilha---")
          print("1 - Checar se está vazia ou não")
          print("2 - Empilhar")
          print("3 - Desempilhar")
          print("4 - Informar tamanho da pilha")
          print("5 - Listar pilha")
          print("6 - Sair")

          opcao = int(input("\nInforme a opção: "))

          if opcao == 1:
              minha_pilha.vazia()
          elif opcao == 2: 
              conteudo_informado = int(input("\nDigite o índice do elemento que você deseja inserir: "))
              data = data.sample(100)
              minha_pilha.empilhar(data.iloc[conteudo_informado]) 
          elif opcao == 3:
              minha_pilha.desempilhar() 
          elif opcao == 4:
              print("Tamanho da pilha é de {} elementos\n".format(minha_pilha.tamanho())) 
          elif opcao == 5:
              minha_pilha.listar()
          elif opcao == 6:
              print("Até a próxima! :D\n")
              break
          else:
              print("Opção inválida, digite uma opção mostrada no menu!\n")

#inciando a função passando a variável 'data'
stackMenu(data)
